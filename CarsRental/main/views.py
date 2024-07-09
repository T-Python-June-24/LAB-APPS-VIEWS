from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
import string , random

# Create your views here.
def welcome_page(request:HttpResponse):
    welcome="Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    today_date="2024/7/7"
    return render(request ,'main/welcome.html',context={'welcome':welcome ,"today_date":today_date})

def about_page(request:HttpResponse):
    about= '''A simple paragraph about Car Rentals.
    -car rental is a service that is beneficial for providing vehicles to people on rent for a short period. It is the hiring of vehicles from one party to another.
       Rents are based on the time you need the vehicles for some hours, daily, weekly and monthly.
    '''
    return render(request ,'main/about.html',context={'about':about})


def password_page(request:HttpResponse):
    symbols="!@#$%^&*()_-+=[]{}|;:,.<>?/"
    characters = string.ascii_letters +symbols+ string.digits
    password = ''.join(random.choice(characters) for i in range(10))
    return render(request ,'main/password_generator.html',context={"password_generator":password})


# def home(request):
#     return render(request,"main/base.html")

# def about(request):
#     return render(request, 'about.html')

# def password_generator(request):
#     return render(request, 'password_generator.html')