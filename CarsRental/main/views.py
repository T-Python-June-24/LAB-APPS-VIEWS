from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
import random
import string


# Create your views here.
def index_website(Http_RQ:HttpRequest):
    return HttpResponse("<center><h1 style= color:blue>Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.</h1></center>")
def about(Http_RQ:HttpRequest):
    return HttpResponse("<center><h1 style= color:blue>A simple paragraph about Car Rentals. </h1></center>")
def password_generate(Http_RQ:HttpRequest):
    sentence = string.ascii_letters + string.digits  
    Complete_sentence = ''.join(random.choice(sentence) for _ in range(10))
    editsentence=f"<center><h1 style= color:blue>{Complete_sentence}</h1></center>"
    return HttpResponse(editsentence)