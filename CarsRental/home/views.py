from django.shortcuts import render
from django.http import HttpResponse
import string , random 

def welcome_view(request:HttpResponse):

    return render(request,"home/welcome.html")


def about_view(request:HttpResponse):

    return render(request,"home/about.html")

def generate_password(request:HttpResponse):

    symbols = '@$*()_-+={[}]|:;,.?'
    chars = string.ascii_letters +symbols+ string.digits
    password = ''.join(random.choice(chars) for i in range(10))

    return render(request,"home/password.html",context={"password":password})

# Create your views here.
