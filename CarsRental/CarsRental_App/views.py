from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string

def home_view(request : HttpRequest):
    content = "<h1>Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.</h1>"
    return HttpResponse(content)

def about_view(request:HttpRequest):
    content = "A simple paragraph about Car Rentals."
    return HttpResponse(content)

def pwGenerator_view(request:HttpRequest):
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return HttpResponse(password)