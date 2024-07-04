from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random, string



def home_view(request:HttpRequest):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")


def about_view(request:HttpRequest):
    return HttpResponse("A simple paragraph about Car Rentals.")


def pass_generator(request:HttpRequest):

    chars = string.ascii_letters + string.digits + string.punctuation

    passGen = ''.join(random.choice(chars) for _ in range(10))

    return HttpResponse(passGen)
