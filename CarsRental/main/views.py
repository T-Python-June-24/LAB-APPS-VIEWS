from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string

# Create your views here.
def home_view(request: HttpRequest):
  return render(request, "main/home.html")

def about_view(request: HttpRequest):
  return render(request, "main/about.html")

def password_generator_view(request: HttpRequest):
  all_characters = string.ascii_letters + string.digits + string.punctuation
  length = 10
  password = ''.join(random.choices(all_characters, k=length))
  return render(request, "main/password_generate.html", {"password": password})


