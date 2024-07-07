import random
import string
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render 



def homePage(request):
    return render(request, 'abdullahApp/home.html')

def aboutPage(request):
    return render(request, 'abdullahApp/about.html')

def passwordPage(request):
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))
    return render(request, 'abdullahApp/password.html', {'password': password})

