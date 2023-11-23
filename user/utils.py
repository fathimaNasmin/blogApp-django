from django.core.mail import send_mail, EmailMultiAlternatives
from email.utils import formataddr
from django.conf import settings

from django.forms.models import model_to_dict
from django.utils.html import strip_tags
from django.template.loader import render_to_string


def send_profile_update_mail(user_profile):
    """ 
    Send mail method on user profile is updated.
    """
    
    # Django mail template
    
    # Use a custom display name and email address
    sender_name = "BlogApp"
    sender_email = settings.EMAIL_HOST_USER
    from_email = formataddr((sender_name, sender_email))

    subject, to = "Profile Updation Notification", user_profile.email
    html_message = render_to_string('user/email_templates/profile_update.html', 
                                    {'firstname':user_profile.first_name,
                                     'lastname':user_profile.last_name})
    plain_message = "Profile Update Notification"
    msg = EmailMultiAlternatives(subject, plain_message, from_email, [to])
    msg.attach_alternative(html_message, "text/html")
    msg.send()
    
    
    
def user_model_fields_changed(new_instance, original_instance, fields):
    """
    Check if specific fields in a model instance have changed.
    """
    new_model_dict = model_to_dict(new_instance,fields=fields)
    original_model_dict = model_to_dict(original_instance, fields=fields)
    return any(new_model_dict[field] != original_model_dict[field] for field in fields)
