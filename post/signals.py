from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from .tasks import send_mail_newsletter_task


@receiver(post_save, sender=Post)
def send_newsletter(sender, instance, created, **kwargs):
    if created:
        send_mail_newsletter_task.delay(instance.id)