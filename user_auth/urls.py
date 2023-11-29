from django.urls import path
from .views import welcome_user, HomeView

urlpatterns = [
    # path('', HomeView.as_view(), name='index'),
	path("", welcome_user, name="user_auth"),
]
