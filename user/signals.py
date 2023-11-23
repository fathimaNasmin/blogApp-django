from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver,Signal
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings

from user.utils import user_model_fields_changed,send_profile_update_mail


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signals to create a profile instance for the new user and 
    send mail to the user.
    """
    if created:
        Profile.objects.create(user=instance)
        
        # Send mail: Welcoming the new User
        
        subject = 'Welcome to Our Website'
        message = "Welcome to Our Website.\nThank you for registering on our website. We hope you'll enjoy your stay!"
        from_email = None
        mail_to = [instance.email]
        
        send_mail(
            subject,
            message,
            from_email,
            mail_to,
            fail_silently=False,
            auth_user=settings.EMAIL_HOST_USER,
            auth_password=settings.EMAIL_HOST_PASSWORD
        )


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()


# Custom signal for user profile update
user_profile_updated = Signal()

@receiver(user_profile_updated)
def handle_user_profile_update(sender, instance, **kwargs):
    # Get the original instance from the database
    original_instance = sender.objects.get(pk=instance.pk)
    # Check if user profile is updated
    if user_model_fields_changed(original_instance, instance, ['first_name','last_name', 'password','profile_image']):
        send_profile_update_mail(original_instance)