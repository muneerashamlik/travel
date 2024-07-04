from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect


# Create your views here.


# nxt (class 41)login

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not none:
            auth.login(request, user)
            return redirect('/')
        else:
            message.info(request, "invalid NEWAPP")
            return redirect(login)
    return render(request, "login.html")


# class registrn
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save();
                return redirect('login')
            # print("user created")
        # (class 38)else:
        # print("password not matching")
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


# class42
def logout(request):
        auth.logout(request)
        return redirect('/')
