from django.conf.urls.static import static
from django.urls import include, path
from user import views as user_view
from django.conf import settings

app_name = 'user'
urlpatterns = [
    path('signup/', user_view.signup, name='signup'),
    path('login/', user_view.login_user, name='login'),
    path('logout/', user_view.logout_user, name='logout'),
]
