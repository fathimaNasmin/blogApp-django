from django.core.mail import send_mail
from django.conf import settings
from django.core.mail.backends.console import EmailBackend

from django.forms.models import model_to_dict

def send_profile_update_mail(user_profile):
    """ 
    Send mail method on user profile is updated.
    """
    console_backend = EmailBackend()
    
    subject = 'Profile Update Notification'
    message = 'Profile Update Notification.\nYour profile has been updated. Thank you for using our service.'
    from_email = 'blogApp@webapplication.com'
    mail_to = [user_profile.email]
    
    send_mail(
        subject,
        message,
        'blogApp@webapplication.com',
        mail_to,
        fail_silently=False,
        auth_user=settings.EMAIL_HOST_USER,
        auth_password=settings.EMAIL_HOST_PASSWORD,
        connection=console_backend
    )
    
    
    
def user_model_fields_changed(new_instance, original_instance, fields):
    """
    Check if specific fields in a model instance have changed.
    """
    new_model_dict = model_to_dict(new_instance,fields=fields)
    original_model_dict = model_to_dict(original_instance, fields=fields)
    print("new model:", new_model_dict)
    print("original model:", original_model_dict)
    return any(new_model_dict[field] != original_model_dict[field] for field in fields)
