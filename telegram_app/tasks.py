from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(email):
    subject = "Welcome!"
    message = "Thank you for registering with our Telegram bot."
    from_email = settings.DEFAULT_FROM_EMAIL  # Use from settings
    recipient_list = [email]

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )
