# 🤖 Django Telegram Bot Integration Project

This project is a Django-based backend integrated with a Telegram bot. It includes user registration via Telegram, email confirmation using Celery and Redis, and REST API endpoints with authentication.

---

## 🗖️ Features

* Telegram bot integration using `python-telegram-bot`
* Stores Telegram usernames in the database
* Asks for email and sends a confirmation message asynchronously using Celery
* REST API with one public and one protected endpoint
* Token-based authentication (TokenAuth)
* Admin panel to view registered users

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/pavan082005/Django-intern-assignment.git
cd Django-intern-assignment
```

### 2. Create Virtual Environment & Activate It

```bash
python -m venv env
env\Scripts\activate       # On Windows
# source env/bin/activate  # On Linux/Mac
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4. Create `.env` File

Create a `.env` file in the root directory and add the following:

```env
SECRET_KEY=your_django_secret_key
DEBUG=False

TELEGRAM_BOT_TOKEN=your_telegram_bot_token

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_app_password

CELERY_BROKER_URL=redis://localhost:6379/0
```

> ⚠️ Be sure to add `.env` to your `.gitignore` file.

---

### 5. Apply Migrations & Create Superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

### 6. Start Redis Server

Make sure Redis is installed and running:

```bash
redis-server
```

> On Windows, navigate to your Redis folder and run `redis-server.exe`.

---

### 7. Start Celery Worker

```bash
celery -A config worker --loglevel=info --pool=solo
```

---

### 8. Start Telegram Bot

```bash
python telegram_bot/bot.py
```

Your Telegram bot will now be active and listening for `/start` commands.

---

### 9. Use Django Shell Instead of Development Server

Since `DEBUG=False`, the development server is disabled. Use the shell for testing or admin tasks:

```bash
python manage.py shell
```

You can use the Django admin panel at your configured production URL or expose one if needed.

---

## 🔑 Environment Variables Summary

```env
SECRET_KEY
DEBUG
TELEGRAM_BOT_TOKEN
EMAIL_HOST
EMAIL_PORT
EMAIL_USE_TLS
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
CELERY_BROKER_URL
```

---

## 🚀 Using the Telegram Bot

1. Open Telegram and search for your bot by username.
2. Send `/start` to begin.
3. The bot will store your Telegram username.
4. It will ask for your email.
5. A welcome email will be sent asynchronously.

---

## 🔮 API Documentation

### 🔓 Public Endpoint

```
GET /api/public/
```

**Response:**

```json
{
  "message": "This is a public endpoint."
}
```

---

### 🔒 Protected Endpoint

```
GET /api/protected/
Authorization: Token <your_token>
```

**Response:**

```json
{
  "message": "This is a protected endpoint.",
  "user": "your_username"
}
```

---

### 🔑 Obtain Auth Token

```
POST /api-token-auth/
```

**Request:**

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**

```json
{
  "token": "your_generated_token"
}
```

---

## 📧 Email Sent by Bot

After you submit your email, the bot sends a message like:

```
Subject: Welcome!
Body: Thank you for using our bot!
From: your_email@gmail.com
```

---

## 🤖 Creating Your Bot Token

1. Open [@BotFather](https://t.me/BotFather) on Telegram.
2. Run `/newbot` and follow the prompts.
3. Copy the generated token and add it to your `.env` file.

---

## 👤 Author

**M Pavan Kumar**
Email: [pavan082005@gmail.com](mailto:pavan082005@gmail.com)
Telegram: [@notalone008](https://t.me/notalone008)

---

