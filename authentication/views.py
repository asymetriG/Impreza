from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import User as CustomUserModel 
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login

def index(request):
    return render(request,"utils/index.html")


def register(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        birth_date = request.POST.get('birthdate')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        phone_number = request.POST.get('phone')

        
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=name,
            last_name=surname
        )
        
        custom_user = CustomUserModel(
            username=username,
            email=email,
            first_name=name,
            last_name=surname,
            birth_date=birth_date,
            gender=gender,
            location=location,
            phone_number=phone_number
        )
        
        custom_user.save()

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            django_login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('authentication:index')  

    return render(request, "authentication/register.html")


def login(request):
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            
            django_login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index') 
        
        else:
            messages.error(request, "Login not successful!")
            return redirect(('authentication:login'))
    else:
        
        return render(request,"authentication/login.html")