from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random
import string
# Create your views here.


def homepage(request: HttpRequest):
    return HttpResponse("""
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #f6d365, #fda085);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: rgba(255, 255, 255, 0.9);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                text-align: center;
            }
            h1 {
                color: #2c3e50;
            }
            p {
                color: #34495e;
            }
            .nav {
                margin-top: 20px;
            }
            .nav a {
                margin: 0 10px;
                color: #3498db;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello World</h1>
            <p>This is my new HOME for Car Rentals Website! We're excited to welcome you here.</p>
            <div class="nav">
                <a href="/about">About</a>
                <a href="/password/generate">Generate Password</a>
            </div>
        </div>
    </body>
    </html>
    """)


def aboutpage(request: HttpRequest):
   
    return render(request, "lab_app/about.html")


def password_generate(request: HttpRequest):
    random_password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))
    
    return render(request, "lab_app/password_generate.html", {"random_password": random_password})