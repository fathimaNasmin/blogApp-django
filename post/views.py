from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json

from django.http import JsonResponse

from user.models import User,Profile



# Create your views here.
def home(request):
    all_post = Post.objects.all().order_by('-date_posted')
    # first_post = all_post[:1]
    # rest_of_posts = all_post[1:]
    # Setup paginator
    paginator = Paginator(all_post, 7)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'post/home.html', {'posts': posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    posted_comments = Comment.objects.filter(post__id=post_id)
    posted_comments_order = posted_comments.order_by('-date_added')[:5]
    post_count = posted_comments.count()
    post_likes = post.like_set.count()
    liked = Like.objects.filter(post=post,user=request.user).exists()
    if request.user:
        current_user = request.user
    return render(request, 'post/post_detail_view.html', {'post': post,
                                                          'current_user': current_user,
                                                          'comments': posted_comments_order,
                                                          'num_of_comments': post_count,
                                                          'num_of_likes':post_likes,
                                                          'user_liked': liked})
    


def like_unlike_post(request,post_id):
    """like/unlike the specific post by the current user"""
    user = request.user
    response = {}

    if request.method == 'POST':
        data = json.loads(request.body)
        print('request.POST:',data)
        post = Post.objects.get(id=data.get('post_id'))
        like_user_post = Like.objects.filter(user=user, post=post)
        print('like_user_post:',like_user_post)
        try:
            if not like_user_post.exists():
                # create a new instance
                new_like_instance = Like.objects.create(user=user,post=post)
                new_like_instance.save()
                print("Created new instance")
                response['created'] = True
            else:
                # remove the existing
                like_user_post.delete()
                print("deleted the instance")
                response['created'] = False
        except Exception as e:
            response['success'] = False
            response['message'] = str(e)
        else:
            response['success'] = True
            response['num_likes'] = post.like_set.count()
        return JsonResponse(response,safe=False)
    


@login_required
def create_new_post(request, pk):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            sub_title = form.cleaned_data['sub_title']
            description = form.cleaned_data['description']
            image_post = form.cleaned_data['image_post']
            print(image_post)
            new_post = Post(title=title, sub_title=sub_title, description=description,
                            image_post=image_post, user=request.user)
            new_post.save()
            return redirect('post:home')
    else:
        form = forms.CreatePost()
    return render(request, 'post/create_blog_post.html', {'form': form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.user:
        messages.error(request, 'You do not have permission to edit this post.')
        return redirect('post:post-detail-view', post_id=post.id)
    if request.method == 'POST':
        form = forms.PostEditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated.')
            return redirect('post:post-detail-view', post_id=post.id)
    else:
        form = forms.PostEditForm(instance=post)
    return render(request, 'post/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    print("delete method called")
    post.delete()
    return redirect('post:home')


@login_required
def view_my_blogs(request, pk):
    my_post = Post.objects.filter(user_id=pk)
    print(my_post)
    return render(request, 'post/my_blogs.html', {'my_blogs': my_post})


@login_required
def comment_post(request, post_id):
    current_post = Post.objects.get(id=post_id)
    print(post_id)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            print(comment)
            new_comment = Comment(comment=comment, user_comment=request.user, post=current_post)
            new_comment.save()
            return redirect('post:post-detail-view', post_id=current_post.id)
    else:
        form = forms.CommentForm()
    return render(request, 'post/comment_post.html', {'form': form, 'post': current_post})


