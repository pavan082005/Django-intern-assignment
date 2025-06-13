import os
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()  # If you're using a .env file

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # You can hardcode or dynamically manage this

bot = Bot(token=TELEGRAM_TOKEN)

def send_telegram_message(message: str):
    if CHAT_ID:
        bot.send_message(chat_id=CHAT_ID, text=message)
    else:
        raise ValueError("Telegram CHAT_ID is not set.")
