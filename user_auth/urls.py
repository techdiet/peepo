from django.urls import path
from .views import welcome_user

urlpatterns = [
	path("", welcome_user, name="user_auth"),
]
