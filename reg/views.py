from django.shortcuts import render,redirect
from django.contrib import messages
#from .models import Register
from django.contrib.auth.models import User,auth

# Create your views here.
def signin(request):
    if request.method =='POST':
        username=request.POST['your_name']
        password=request.POST['your_pass']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("pglist")
        else:
            messages.info(request,'invalid credentials')
            return redirect('signin')

    else:
        return render(request,'signin.html')


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['pass']
        password2=request.POST['re_pass']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('signin')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
