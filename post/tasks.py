from django.core.mail import send_mass_mail
from smtplib import SMTPException

from django.conf import settings
from celery import shared_task

from newsletter.models import Subscriber
from .models import Post


@shared_task()
def send_mail_newsletter_task(post_id):
    """Sends email to all subscribers."""
    post = Post.objects.get(id=post_id)
    subscribers = Subscriber.objects.all()
    
    subject = f"New Blog added from {post.category.name} category"
    message = f"Check out our latest blog post:\n\n \
                {post.title} by {post.user.profile.full_name}"
                
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [subscriber.email for subscriber in subscribers]
    
    message_list = [(subject, message, from_email, [recipient])
                    for recipient in recipient_list]
    
    try:
        send_mass_mail(tuple(message_list),fail_silently=True)
        print("mail sent by celery for all subscribers")
    except SMTPException as e:
        print(f"An SMTP error occurred: {e}")
