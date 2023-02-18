from django.db import models
from user.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=300)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image_post = models.ImageField(upload_to='post_images', null=True, blank=True)# default='post_default.jpg',
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username, self.title} Post'


class Comment(models.Model):
    comment = models.TextField()
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username, self.title} Comment'
