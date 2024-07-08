from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import random
import string

def home(request):

    return render(request, "Cars/home.html")

def about(request):
  
    return render(request, "Cars/about.html")

def generate_password(request):

    password_length = 10

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    
    return render(request, "Cars/generate_password.html", context= {"password" : password})
