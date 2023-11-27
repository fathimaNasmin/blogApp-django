from django.urls import include, path
from post import views as post_view

app_name = 'post'
urlpatterns = [
    path('', post_view.home, name='home'),
    path('view/<int:post_id>/', post_view.post_detail_view, name='post-detail-view'),
    path('comment/<int:post_id>/', post_view.comment_post, name='comment-post'),
    path('view/<int:post_id>/get-more-comments/',
         post_view.get_more_comments, name='get-more-comments'),

    path('<int:pk>/create/', post_view.create_new_post, name='create-new-post'),
    path('edit/<int:post_id>/', post_view.edit_post, name='edit-post'),
    path('delete/<int:post_id>/', post_view.delete_post, name='delete-post'),
    path('myblogs/<int:pk>/', post_view.view_my_blogs, name='my-blogs'),
    path('myblogs/<int:pk>/', post_view.view_my_blogs, name='my-blogs'),
    
    path('view/<int:post_id>/like/', post_view.like_unlike_post, name='like-unlike-post'),



]