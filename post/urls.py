from django.urls import include, path
from post import views as post_view

app_name = 'post'
urlpatterns = [
    path('', post_view.home, name='home')
]