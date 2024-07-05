from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import random
import string

# Create your views here.
def main_view(request : HttpRequest):
    content = '''
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>White Box on Sky Background</title>
    <style>
        body {
            background-color: #87CEEB; /* Sky Blue background */
            margin: 0; /* Remove default margin */
            padding: 0; /* Remove default padding */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Full viewport height */
            font-family: Arial, sans-serif;
        }
        .white-box {
            background-color: #fff; /* White box background */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1); /* Optional: Adds a subtle shadow */
            max-width: 80%; /* Optional: Limits the width of the box */
            text-align: center;
        }
        .nav a {
                margin: 0 10px;
                color: #3498db;
                text-decoration: none;
            }
        .h1{
        color:#1687A7
        }
    </style>
</head>
<body>
    <div class="white-box">
        <h1>Hello World,</h1>
        <p>This is our new HOME for Car Rentals Website! We're excited to welcome you here.</p>
                 <div class="nav">
                <a href="/about">About</a>
                <a href="/password/generate/">Password</a>
                </div>
    </div>
    
</body>
</html>
'''
   
    return HttpResponse (content)

def about_view(request : HttpRequest):
    content = '''
     <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            background-color: #87CEEB;
            margin: 20px; /* Remove default margin */
            padding: 20px; /* Remove default padding */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; 
            font-family: Arial, sans-serif;
        }
        .white-box {
            background-color: #fff; /* White box background */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1); /* Optional: Adds a subtle shadow */
            max-width: 80%; /* Optional: Limits the width of the box */
            text-align: center;
        }
        .nav a {
                margin: 0 10px;
                color: #3498db;
                text-decoration: none;
            }
    </style>
</head>
<body>

    <div class="white-box">
        <h1>Welcome to Our Cars Rental Page</h1>
        <p>Cars rental is a ticket to write your own story - a story of exploration, where the destination is just the beginning.
                Whether you're chasing sunsets along coastal highways or navigating bustling city streets, your rented car becomes 
                 more than transportation; it becomes your trusted companion on a voyage of discovery.</p>
                 <div class="nav">
                 <a href="/">Home</a>
                <a href="/password/generate/">Password</a>
                </div>
    </div>
    
</body>
</html>

    '''
    
    return HttpResponse (content)



def generate_password(request: HttpRequest):
    # Define the character sets
    letters = string.ascii_letters  # includes both uppercase and lowercase letters
    symbols = string.punctuation  # includes common symbols
    digits = string.digits  # includes digits 0-9

    # Combine all characters
    all_characters = letters + symbols + digits

    # Generate a password using random choices
    password = ''.join(random.choices(all_characters, k=10))
    result = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #87CEEB;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .whiteBox {{
                background-color: rgba(255, 255, 255, 0.9);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                text-align: center;
            }}
            h1 {{
                color: #2c3e50;
            }}
            .password {{
                background-color: #DFF8FE;
                font-size: 24px;
                color: #003458;
                margin-top: 20px;
            }}
            .nav {{
                margin-top: 20px;
            }}
            .nav a {{
                margin: 0 10px;
                color: #3498db;
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <div class="whiteBox">
            <h2>This is a 10 char big, small, symbol generated password</h2>
            <p class="password">{password}</p>
            <div class="nav">
                <a href="/">Home</a>
                <a href="/about">About</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(result)
    


