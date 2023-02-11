from django.contrib import admin
from django.contrib.auth.models import User
from post.models import Post, Comment
from user.models import Profile
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
