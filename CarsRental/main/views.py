from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string

# Create your views here. 

def page_view(request: HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website! We're excited to welcome you here."
    return HttpResponse(content)

def about_view(request: HttpRequest):
    content = '''<h3>A simple paragraph about Car Rentals:</h3>
    Car rentals offer a convenient and flexible transportation option for travelers and individuals in need of a temporary vehicle. 
    Whether for a business trip, vacation, or while a personal car is being repaired, rental services provide access to a wide range of vehicles to suit various needs and preferences. 
    Customers can choose from economy cars for cost-effective travel, luxury vehicles for special occasions, or larger vehicles like SUVs and vans for family trips and group travel. 
    With options for short-term and long-term rentals, car rental companies cater to diverse requirements, ensuring mobility and convenience wherever one needs to go.
    '''
    return HttpResponse(content)

def password_view(request: HttpRequest):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(10))
    return HttpResponse(password)
