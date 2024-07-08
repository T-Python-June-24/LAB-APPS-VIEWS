from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string
import datetime

def home_view(request : HttpRequest):

    return render(request, "main/home.html")

def about_view(request: HttpRequest):

    return render(request, "main/about.html")

def about_view(request: HttpRequest):
    date = datetime.datetime.now()
    return render(request, "main/about.html" , context ={"date_time":date})

def pwGenerator_view(request:HttpRequest):
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    return render(request, "main/passwordGenerator.html", context={"password": password})