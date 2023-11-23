from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver,Signal
from .models import Profile

from django.conf import settings

from django.core.mail import send_mail, EmailMultiAlternatives
from email.utils import formataddr

from django.template.loader import render_to_string

from user.utils import (user_model_fields_changed,
                        send_profile_update_mail)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signals to create a profile instance for the new user and 
    send mail to the user.
    """
    if created:
        Profile.objects.create(user=instance)
        
        # Send mail: Welcoming the new User
        sender_name = "BlogApp"
        sender_email = settings.EMAIL_HOST_USER
        from_email = formataddr((sender_name, sender_email))

        subject, to = "New Account Created", instance.email
        html_message = render_to_string('user/email_templates/welcome_email.html',
                                        {'firstname': instance.first_name,
                                        'lastname': instance.last_name})
        plain_message = "New Account Created"
        msg = EmailMultiAlternatives(subject, plain_message, from_email, [to])
        msg.attach_alternative(html_message, "text/html")
        msg.send()


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