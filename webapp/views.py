from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, "pages/home.html", {})

def login_page(request):
    return render(request, "pages/auth/login.html", {})

def register_page(request):
    return render(request, "pages/auth/register.html", {})