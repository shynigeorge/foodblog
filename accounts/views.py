from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def registered(request):

    if request.method=="POST":

        fname=request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1= request.POST['psw']
        password2= request.POST['psw-repeat']

        if password1==password2:
            if User.objects.filter(username=username ).exists():
                messages.info(request,"username  taken")
                return redirect('registered')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('registered')
            else:
                user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password1)
                user.save();
                print("user created")
        else:
            print("password not matched")
            return redirect('registered')
        return redirect('/')
    else:
        return render(request,'register.html')
def loged(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            
            return redirect('/')
        else:
            messages.info(request,"invalid details")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
