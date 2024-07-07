import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import matplotlib.pyplot as plt
import io

def create_graph():
    # Sample data
    years = ['2022', '2023', '2024']
    rentals = [700, 670, 900]

    plt.figure(figsize=(8, 6))
    plt.bar(years, rentals, color='green')
    plt.xlabel('year')
    plt.ylabel('Rentals')
    plt.title('Car Rentals Market')


    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf


from django.shortcuts import render
from django.http import HttpResponse ,HttpRequest
import random
import string

# Create your views here.

def home (request:HttpRequest):
    content="Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here"
    return HttpResponse(content)
def about(request):
    graph = create_graph().getvalue()
    return HttpResponse(graph, content_type='image/png')
def password(request:HttpRequest):

    all_characters = string.ascii_letters + string.digits + string.punctuation
    password= ''.join(random.choices(all_characters, k=10))
    return HttpResponse(f"Your Generated Password  : {password}")



