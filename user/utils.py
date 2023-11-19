from django.core.mail import send_mail
from django.conf import settings
from django.core.mail.backends.console import EmailBackend

def custom_register_mail(subject,message,mail_to):
    console_backend = EmailBackend()
    send_mail(
        subject,
        message,
        'from@example.com',
        mail_to,
        fail_silently=False,
        auth_user='learnpy22@gmail.com',
        auth_password=settings.EMAIL_HOST_PASSWORD,
        connection=console_backend
    )
