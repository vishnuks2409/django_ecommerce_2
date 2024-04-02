from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Customers view

def signout(request):
    logout(request)
    return redirect('products:home')


def Show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST['username']
            password=request.POST['password']
            email=request.POST['email']
            address=request.POST['address']
            phone=request.POST['phone']
            # craete user account
            user=User.objects.create_user(username=username,password=password,email=email)

           #create customer account
            customer=Customer.objects.create(
                name=username, 
                user=user,
                phone=phone,
                address=address
                )
    
            success_message="user registered succesfully"
            messages.success(request,success_message)
        except Exception as e:
            error_message="The user name is alreday exist"
            messages.error(request,error_message)

    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('products:home')
        else:
            messages.error(request,'invalid creadentials')


    return render(request,'account.html',context)
