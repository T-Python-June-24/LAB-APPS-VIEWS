from django.shortcuts import render
from django.http import HttpResponse , HttpRequest
import random
import string


# Create your views here.
def homePage(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")


def aboutPage(request):
    return HttpResponse("A simple paragraph about Car Rentals.")


def passwordPage(request):
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))
        return HttpResponse(password)
