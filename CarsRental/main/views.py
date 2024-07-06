from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string

# Create your views here. 

def page_view(request: HttpRequest):
    return render(request, 'home.html')

def about_view(request: HttpRequest):
    return render(request, 'about.html')

def contact_view(request: HttpRequest):
    return render(request, 'contact.html')

def password_view(request: HttpRequest):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(10))
    return render(request, 'password.html', {'password': password})

def cars_view(request: HttpRequest):
    cars = [
        {'name': 'BMW 420i', 'info': 'Model: 2024', 'price': '850 SR/day', 'image_url': '/static/images/BMW 420i.jpg'},
        {'name': 'Genesis GV80', 'info': 'Model: 2022', 'price': '550 SR/day', 'image_url': '/static/images/Genesis GV80.jpg'},
        {'name': 'Ford Taurus', 'info': 'Model: 2024', 'price': '400 SR/day', 'image_url': '/static/images/Ford Taurus.jpg'},
        {'name': 'Audi Q8', 'info': 'Model: 2023', 'price': '700 SR/day', 'image_url': '/static/images/Audi Q8.jpg'},
    ]
    return render(request, 'cars.html', {'cars': cars})