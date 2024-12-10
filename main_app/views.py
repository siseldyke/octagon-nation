from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
# Create your views here.

def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')