from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import random
import string

# Create your views here.
def main_view(request : HttpRequest):
    content = '''
    <body style="background-color: #8BC34A; color: #fff">
        <div style="padding: 20px;">
            <p style="font-family: Arial, sans-serif; font-size: 24px; line-height: 1.5;">
                Hello World, This is my new HOME for Car Rentals Website! We're excited to welcome you here.
            </p>
        <div style="padding: 20px;">
    </body>
    '''
    return HttpResponse (content)

def about_view(request : HttpRequest):
    content = '''
    <body style="background-color: #8BC34A; color: #fff">
        <div style="padding: 20px;">
            <p style="font-family: Arial, sans-serif; font-size: 24px; line-height: 1.5;">
                Cars rental is a ticket to write your own story - a story of exploration, where the destination is just the beginning.
                Whether you're chasing sunsets along coastal highways or navigating bustling city streets, your rented car becomes 
                more than transportation; it becomes your trusted companion on a voyage of discovery.
            </p>
        <div style="padding: 20px;">
    </body>
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
    result = f'''
    <body style="background-color: #8BC34A; color: #fff; /* Green background, white text */">
        <div style="padding: 20px;">
            <p style="font-family: Arial, sans-serif; font-size: 24px; line-height: 1.5;">
                A randomly generated 10-long password of characters (letters, upper, lower, symbols):<br>
                <span style="background-color: yellow; color: red; padding: 5px; border-radius: 5px;">{password}</span>
            </p>
        </div>
    </body>
    '''
    return HttpResponse(result)
    


