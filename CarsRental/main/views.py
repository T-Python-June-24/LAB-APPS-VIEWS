from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import string
import random


# Create your views here.
def home_view(request: HttpRequest):
    return render(request, 'main/home.html')


def about_view(request: HttpRequest):
    return render(request, 'main/about.html')


def generate_password_view(request: HttpRequest):
    password_length = 10
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    return render(request, 'main/password_generate.html', context={'password': password})
