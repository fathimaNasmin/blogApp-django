from django.contrib import admin
from post.models import Post, Comment,Category,Like


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Comment)
