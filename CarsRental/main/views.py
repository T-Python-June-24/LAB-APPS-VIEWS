from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
import string , random

# Create your views here.
def welcome_page(request):
    content="Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_page(request):
    content= '''A simple paragraph about Car Rentals.
    -car rental is a service that is beneficial for providing vehicles to people on rent for a short period. It is the hiring of vehicles from one party to another.
       Rents are based on the time you need the vehicles for some hours, daily, weekly and monthly.
    '''

    return HttpResponse(content)


def password_page(request):
    symbols="!@#$%^&*()_-+=[]{}|;:,.<>?/"
    characters = string.ascii_letters +symbols+ string.digits
    password = ''.join(random.choice(characters) for i in range(10))
    return HttpResponse(password)

