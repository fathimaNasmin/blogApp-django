from django import forms
from .models import Post, Comment


class CreatePost(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_post'].label = "Post Image"

    class Meta:
        model = Post
        exclude = ['user', 'date_posted']

class PostEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_post'].label = "Post Image"

    class Meta:
        model = Post
        exclude = ['user', 'date_posted']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user_comment', 'post']

