from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

@csrf_exempt
def LoginPage(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=uname, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
        
    return render(request, 'login.html')

@csrf_exempt
def RegPage(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        password = request.POST.get('password')
        email=request.POST.get('email')
        my_user=User.objects.create_user(uname,password,email)
        my_user.save()
        return redirect('login')

    
    return render(request,'registration.html')
