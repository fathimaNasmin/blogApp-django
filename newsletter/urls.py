from django.urls import include, path
from newsletter import views as newsletter_view

app_name = 'newsletter'

urlpatterns = [
    path('', newsletter_view.subscribe, name='subscribe'),
]