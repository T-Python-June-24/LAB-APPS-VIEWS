from django.shortcuts import render
from django.http import HttpResponse 
import random
import string
# Create your views here.

def home (request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here")
def about(request):
    return HttpResponse("A simple paragraph about Car Rentals")
def password(request):
    def generate_password(length=10):
        all_characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(all_characters, k=length))
    
    password = generate_password()
    return HttpResponse(f"Your Generated Password  : {password}")