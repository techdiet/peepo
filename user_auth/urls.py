from django.urls import path
from .views import welcome_user, HomeView
from .views import DashboardView

urlpatterns = [
    # path('', HomeView.as_view(), name='index'),
	path("", welcome_user, name="user_auth"),
    path("<pk>/", DashboardView.as_view(), name="dashboard"),
]
