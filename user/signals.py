from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings
from django.core.mail.backends.console import EmailBackend


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
        # Send mail: Welcoming the new User
        console_backend = EmailBackend()
        
        subject = 'Welcome to Our Website'
        message = "Welcome to Our Website.\nThank you for registering on our website. We hope you'll enjoy your stay!"
        from_email = 'webmaster@example.com'
        mail_to = [instance.email]
        
        send_mail(
            subject,
            message,
            from_email,
            mail_to,
            fail_silently=False,
            connection=console_backend
        )
        

# auth_user='learnpy22@gmail.com',
# auth_password=settings.EMAIL_HOST_PASSWORD,

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
