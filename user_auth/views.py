from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import CustomUser
from django.views.generic import DetailView

# Create your views here.
# def index(request):
#     return render(request, 'user_auth/home.html', {})

class HomeView(View):
    def get(self, request):
        return render(request, 'user_auth/home.html', {})

def welcome_user(request):
	return HttpResponse("welcome to peepo")
class DashboardView(DetailView):
      model=CustomUser
      template_name='user_auth/dashboard.html'
      context_object_name='user'
