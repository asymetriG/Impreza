from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as django_login
from hashlib import sha256
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,"utils/index.html")

def register(request):
    if request.method == "POST":
        # Existing fields
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
        
        security_question = request.POST.get('security_question')
        security_question_answer = request.POST.get('security_question_answer')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('authentication:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('authentication:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('authentication:register')
        
        password = sha256(password.encode()).hexdigest()

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=name,
            last_name=surname
        )
        
        custom_user = Profile(
            user=user,
            birth_date=birth_date,
            gender=gender,
            location=location,
            phone_number=phone_number,
            security_question=security_question,
            security_question_answer=security_question_answer
        )
        
        custom_user.save()

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            django_login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('index')  

    return render(request, "authentication/register.html")


def login(request):
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        password = sha256(password.encode()).hexdigest()
        
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
    
def forgot_password(request):
    if request.method == "POST":

        username = request.POST.get("username")
        
        user = User.objects.filter(username=username).first()
        
        if not user:
            messages.error(request, "Username not found.")
            return redirect('authentication:forgot_password')
        

        if 'security_answer' in request.POST:  
            
            answer = request.POST.get("security_answer")
            security_question = request.POST.get("security_question")
            if answer == user.security_question_answer and security_question == user.security_question:

                new_password = request.POST.get("new_password")
                confirm_password = request.POST.get("confirm_password")

                if new_password != confirm_password:
                    messages.error(request, "Passwords do not match.")
                    return redirect('authentication:forgot_password')


                user.password = sha256(new_password.encode()).hexdigest()
                user.save()
                
                auth_user = User.objects.get(username=username)
                auth_user.set_password(sha256(new_password.encode()).hexdigest())
                auth_user.save()

                messages.success(request, "Password reset successful!")
                return redirect('authentication:login')
            else:
                messages.error(request, "Incorrect answer to the security question.")
                return redirect('authentication:forgot_password')

        return render(request, "authentication/forgot_password.html")

    return render(request, "authentication/forgot_password.html")
 
 
@login_required
def my_profile(request):
    
    user = User.objects.get(username=request.user.username)
    
    return render(request, "authentication/my_profile.html", {"user": user})

@login_required
def change_profile_picture(request):
    if request.method == 'POST' and request.FILES.get('profile_picture'):
        profile_picture = request.FILES['profile_picture']

        profile = Profile.objects.get(user=request.user)
        profile.profile_picture = profile_picture
        profile.save()
        
        messages.success(request, "Profile picture updated successfully!")
    else:
        messages.error(request, "Please select a valid image file.")

    return redirect('authentication:my_profile')

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('index') 

