
from django.shortcuts import render
from django.http import HttpResponse ,HttpRequest
import random
import string

# Create your views here.

def home (request:HttpRequest):
    return render(request,"main/home.html")
def about(request):

    return render(request,"main/about.html")
def password(request:HttpRequest):

    all_characters = string.ascii_letters + string.digits + string.punctuation
    password= ''.join(random.choices(all_characters, k=10))
    return render(request,"main/password.html",context={"password":password})



