from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        pwd=request.POST['pwd']
        user=auth.authenticate(username=username,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")
    return render(request,"login.html")
def register(request):
    if request.method =='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        pwd=request.POST['pwd']
        pwd1=request.POST['cpwd']
        if pwd==pwd1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is taken, Choose another")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is taken, Choose another")
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username,password=pwd,
                    first_name=first_name,last_name=last_name,
                    email=email,
                )
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"password is taken")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')