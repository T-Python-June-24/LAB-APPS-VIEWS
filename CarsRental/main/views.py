from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string

# Create your views here.
def page_view(request: HttpRequest):
  content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
  return HttpResponse(content)

def about_view(request: HttpRequest):
  content = "A simple paragraph about Car Rentals. "
  return HttpResponse(content)

def password_generator_view(request: HttpRequest):
  all_characters = string.ascii_letters + string.digits + string.punctuation
  length = 10
  password = ''.join(random.choices(all_characters, k=length))
  return(HttpResponse(password))


