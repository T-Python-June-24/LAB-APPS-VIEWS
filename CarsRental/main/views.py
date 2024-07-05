from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import string
import random
# Create your views here.
def home_view(request: HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request: HttpRequest):
    content = "A simple paragraph about Car Rentals."
    return HttpResponse(content)

def generate_password_view(request: HttpRequest):
    password_length = 10
    content = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    return HttpResponse(content)
