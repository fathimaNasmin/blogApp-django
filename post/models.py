from django.db import models
from user.models import User
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=300)
    description = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image_post = models.ImageField(upload_to='post_images', null=True, blank=True)# default='post_default.jpg',
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name, self.title} Post"


class Like(models.Model):
    """Model to store the likes for a post"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"
    
    
    
class Comment(models.Model):
    # comment = models.TextField()
    comment = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_comment.username, self.post.title} Comment'
