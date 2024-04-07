# URL patterns for authentication endpoints like /register, /login, /logout.
# These URLs will be included in the main project's urls.py file.

from django.urls import path
from .views import RegisterView, LoginView, LogoutView, DeleteUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('delete_user/', DeleteUserView.as_view(), name='auth_delete_user'),
]
