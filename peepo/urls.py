"""
URL configuration for peepo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
	path("auth/", include("user_auth.urls"), name="user_auth"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html") , name="login"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="registration/reset_pass_form.html") , name="password_reset"),
    path("reset/confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view() , name="password_reset_confirm"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"),
    path("password_reset/confirm/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("", TemplateView.as_view(template_name="home.html"), name="index"),
]

