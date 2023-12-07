from time import sleep
from django.core.mail import send_mail
from smtplib import SMTPException

from django.conf import settings
from celery import shared_task


@shared_task()
def send_subscription_email_task(email_address):
    """Sends an email when the user subscribe for the newsletter."""
    sleep(20)  # Simulate expensive operation(s) that freeze Django
    try:
        send_mail(
            "Newsletter Subscription",
            f"You've been subscribed for receiving newsletter from Blog App",
            settings.EMAIL_HOST_USER,
            [email_address],
            fail_silently=False,
        )
        print("mail sent by celery")
    except SMTPException as e:
        print(f"An SMTP error occurred: {e}")
