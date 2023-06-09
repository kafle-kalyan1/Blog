

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
# import authencate
from django.contrib.auth import authenticate, login , logout

# Create your views here.
def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not User.objects.filter(email=email).exists():
            messages.error(request, 'User Not found please register')
            return redirect('login')
        # authencate password now
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is None:
            messages.warning(request, 'Incorrect Password')
            return redirect('login')
        else:
            login(request, user)
            return redirect('../blog/') 

    return render(request, "Account/Login.html")


def registerHandller(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        userEx = User.objects.filter(email=email)
        if userEx.exists():
            messages.warning(request, 'Email already exist')
            return redirect('registerHandller')

        user = User.objects.create(
           username = email,
            first_name=first_name,
            last_name = last_name,
            email=email,
        )
        user.set_password(password)
        user.save()

        messages.success(request, 'Register sucess now login')

        return redirect('login')
    return render(request, "Account/Register.html")
     
def logoutN(request):
    if 'user' in request.session:
        del request.session['user']
    logout(request)
    return redirect('login')
