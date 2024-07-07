from django.shortcuts import render
import random
import string



def home(request):
    message = "Hello World, This is my new HOME for Car Rentals Website  ! We're excited to welcome you here."
    return render(request, 'home.html', {'message': message})



def about(request):
    about_text = "Hello There, \n welcome to our Car Rentals portal \n It's our pleasure to serve you \n our cars rental range start from 100 SR a day to serve your needs \n If you're looking for a luxerious car we can serve you with that as well"
    return render(request, 'about.html', {'about_text': about_text})



def generate_password(request):
    password_length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    return render(request, 'password.html', {'password': password})
