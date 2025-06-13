from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):  # 👈 ADD THIS PARAMETER
    send_mail(
        'Welcome!',
        'Thanks for registering!',
        'pavan082005@gmail.com',
        [email],  # 👈 USE THE PARAMETER HERE
        fail_silently=False,
    )
