from django.conf.urls.static import static
from django.urls import include, path
from user import views as user_view
from django.conf import settings

app_name = 'user'
urlpatterns = [
    path('signup/', user_view.signup, name='signup'),
    path('login/', user_view.login_user, name='login'),
    path('logout/', user_view.logout_user, name='logout'),
    path('<int:pk>/myprofile/', user_view.my_profile, name='my-profile'),
    path('<int:pk>/change_password/', user_view.change_password, name='change-password'),
    path('<int:pk>/delete/', user_view.delete_profile, name='delete-profile'),
]
