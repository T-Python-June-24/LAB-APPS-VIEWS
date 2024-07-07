from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def home(request):
  message = "Hello World, This is my new HOME for Car Rentals Website  ! We're excited to welcome you here."
  return HttpResponse(message)  # Directly return the message

def about(request):
  about_text = " Hello There, \n Thank you for choosing our Cars Rental Portal \n we have plenty of choices that satisfy everyone's needs \n tell us about your expectations to serve you better than you expect"
  return HttpResponse(about_text)

def generate_password(request):
  password_length = 10
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(password_length))
  return HttpResponse(password)
