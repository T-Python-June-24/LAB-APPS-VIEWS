from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import random
import string



def home_view(request:HttpRequest)->render:
    return render(request,"main/home.html")




def about_view(request:HttpRequest)->render:
    return render(request,"main/about.html")




def password_view(request:HttpRequest)->render:
    upperCaseLetters:str=string.ascii_uppercase
    lowerCaseLetters:str=string.ascii_lowercase
    symbols:str=string.punctuation
    digits:int=string.digits
    upper=lower=dig=sym=True
    all="" #where all string , symbole and digit will be concnate
    if upper:
        all+=upperCaseLetters
    if lower:
        all+=lowerCaseLetters
    if dig:
        all+=digits
    if sym:
        all+=symbols
    length=10
    password="".join(random.sample(all,length))



    return render(request,"main/password_genrator.html",context={'password':password})



# Create your views here.
