from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import random
import string

# Create your views here.
def home(request : HttpRequest):
  
    return render (request, "myCarsApp/home.html")

def about_view(request : HttpRequest):
    
    return render(request, "myCarsApp/about.html")



def generate_password(request: HttpRequest):
    # Define the character sets
    letters = string.ascii_letters  # includes both uppercase and lowercase letters
    symbols = string.punctuation  # includes common symbols
    digits = string.digits  # includes digits 0-9

    # Combine all characters
    all_characters = letters + symbols + digits

    # Generate a password using random choices
    password = ''.join(random.choices(all_characters, k=10))
    
    return render(request, "myCarsApp/generate.html", context= {"password": password})
    


