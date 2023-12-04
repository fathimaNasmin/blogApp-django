from django.db import models




class Subscriber(models.Model):
    """Model for Subscriber Emails"""
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return f"Subscriber {self.email}"
