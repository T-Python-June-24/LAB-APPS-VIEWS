from django.shortcuts import render
from django.http import HttpResponse
import string , random 

def welcome_view(request:HttpResponse):

    content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cars rental | Home </title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 5%;
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .menu {
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 20px;
            position: absolute;
            top: 20px;
            right: 20px;
        }

        .menu ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .menu ul li {
            border-bottom: 1px solid #eeeeee;
        }

        .menu ul li:last-child {
            border-bottom: none;
        }

        .menu ul li a {
            display: block;
            padding: 15px 20px;
            text-decoration: none;
            color: #333333;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        .menu ul li a:hover {
            background-color: #007bff;
            color: #ffffff;
        }

        .menu-title {
            background-color: #007bff;
            color: #ffffff;
            padding: 15px 20px;
            font-size: 18px;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1> Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here. </h1>
    <div class="menu">
        <div class="menu-title">Menu</div>
        <ul>
            <li><a href="">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/password/generate">Password Generator</a></li>
        </ul>
    </div>
</body>
</html>

"""

    return HttpResponse(content)


def about_view(request:HttpResponse):

    content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cars rental | About us </title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0 50px 0 50px;
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        h1 {
            position: absolute;
            top: 300px;
            left:50px
        }
        .menu {
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 20px;
            position: absolute;
            top: 20px;
            right: 20px;
        }

        .menu ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .menu ul li {
            border-bottom: 1px solid #eeeeee;
        }

        .menu ul li:last-child {
            border-bottom: none;
        }

        .menu ul li a {
            display: block;
            padding: 15px 20px;
            text-decoration: none;
            color: #333333;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        .menu ul li a:hover {
            background-color: #007bff;
            color: #ffffff;
        }

        .menu-title {
            background-color: #007bff;
            color: #ffffff;
            padding: 15px 20px;
            font-size: 18px;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1> About us </h1>
    <p>Welcome to <b>Cars Rental</b>, your go-to destination for all your car rental needs. 
    Established in 1999 , we have been providing top-notch car rental services to individuals, families, 
    and businesses alike. Our mission is to offer a seamless, hassle-free, 
    and enjoyable car rental experience to our valued customers.</p>
    <div class="menu">
        <div class="menu-title">Menu</div>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/password/generate">Password Generator</a></li>
        </ul>
    </div>
</body>
</html>

"""

    return HttpResponse(content)

def generate_password(request:HttpResponse):

    symbols = '@$*()_-+={[}]|:;,.?'
    chars = string.ascii_letters +symbols+ string.digits
    password = ''.join(random.choice(chars) for i in range(10))

    content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cars rental | Password Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0 50px 0 50px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        h3 {
            display: inline-block;
            background-color:#EEEDEB;
            padding: 20px

        }

        .menu {
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 20px;
            position: absolute;
            top: 20px;
            right: 20px;
        }

        .menu ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .menu ul li {
            border-bottom: 1px solid #eeeeee;
        }

        .menu ul li:last-child {
            border-bottom: none;
        }

        .menu ul li a {
            display: block;
            padding: 15px 20px;
            text-decoration: none;
            color: #333333;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        .menu ul li a:hover {
            background-color: #007bff;
            color: #ffffff;
        }

        .menu-title {
            background-color: #007bff;
            color: #ffffff;
            padding: 15px 20px;
            font-size: 18px;
            text-align: center;
        }

        .refresh-button {
            padding: 10px 20px;
            font-size: 16px;
            color: #ffffff;
            background-color: #007bff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .refresh-button:hover {
            background-color: #0056b3;
        }

        button {
            display: block;
            
        }

    </style>
</head>
<body>

<h1>Generated Password</h1>

<h3>
"""+password+"""
</h3>

<button class="refresh-button" onclick="refreshPage()">New Password</button>
    <div class="menu">
        <div class="menu-title">Menu</div>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/password/generate">Password Generator</a></li>
        </ul>
    </div>
    <script>
        function refreshPage() {
            location.reload();
        }
    </script>
</body>
</html>

"""   

    return HttpResponse(content)
# Create your views here.
