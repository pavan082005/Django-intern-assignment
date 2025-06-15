import os
import sys
import django
import re

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)
from asgiref.sync import sync_to_async
from django.utils.timezone import now

# === Django Setup ===
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# === Django Models & Celery Task ===
from telegram_app.models import TelegramUser
from telegram_app.tasks import send_welcome_email  # Celery task

# === Constants ===
EMAIL = 1

# === Token ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or "your-token-here"

# === DB Operation: Save Telegram User, Return Success ===
@sync_to_async
def save_telegram_user(telegram_id, username):
    if not username:
        return False  # Reject empty username
    user, created = TelegramUser.objects.get_or_create(
        telegram_id=telegram_id,
        defaults={"username": username, "joined_at": now()}
    )
    return True

# === Handlers ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    tg_user = update.effective_user
    username = tg_user.username or tg_user.first_name or ""

    success = await save_telegram_user(chat_id, username)

    if not success:
        await update.message.reply_text("Username not detected. Please set a username in your Telegram profile and try again.")
        return ConversationHandler.END

    await update.message.reply_text(f"Welcome {username}! Please enter your email address to receive a message.")
    return EMAIL

async def email_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    email = update.message.text.strip()

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        await update.message.reply_text("Invalid email format. Please enter a valid email address:")
        return EMAIL

    send_welcome_email.delay(email)  # Send email, don't store it
    await update.message.reply_text(f"A welcome message has been sent to {email}. You are now registered!")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Operation cancelled.")
    return ConversationHandler.END

# === Main Bot Runner ===
def main():
    print("Bot is running...")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, email_handler)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)
    app.run_polling()

if __name__ == "__main__":
    main()
