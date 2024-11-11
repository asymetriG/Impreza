from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout

def administration_panel(request):

    return render(request, "administration/admin_panel.html")


def administration_login(request):
    if request.method == "POST":
        username = request.POST.get('admin_username')
        password = request.POST.get('admin_password')

        if username == "admin" and password == "admin":
            return render(request, "administration/admin_panel.html")
        else:
            messages.error(request, "Login not successful.")
            return redirect('administration:admin_login')
    
    return render(request,"administration/admin_login.html")

def admin_logout(request):
    return render(request,"administration/admin_login.html")
