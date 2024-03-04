from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method ==  'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['user_name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password== confirm_password:
            if User.objects.filter(username= user_name).exists():
                messages.info(request,'user name taken')
                print("user already exit")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("user email already exit")
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name,password=password,email=email,first_name= first_name,last_name=last_name)
                user.save()
                print("account created")
                return redirect('login')
            
        else:
            print('password not matched')
            return redirect('register')
    else:
        return render(request,'register.html')
def login(request):
    if request.method ==  'POST':
        user_name=request.POST['user_name']
        
        password=request.POST['password']
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('travel')
        else:
            messages.info(request,'user name or password is wrong')
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('travel')