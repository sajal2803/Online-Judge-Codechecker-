
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect

def home(request):
    return render(request,"authentication/index.html")

def signup(request):

    if request.method =="POST":
        username= request.post['username']
        fname= request.post['fname']
        lname=request.post['lname']
        email=request.post['eamil']
        pass1=request.post['pass1']
        pass2=request.post['pass2']
       
        myuser =User.ojects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()

        messages.success(request,"Your account created")

        return redirect('signin/')

    return render(request,"authentication/signup.html")


def signin(request):
    return render(request,"authentication/signin.html")

def signout(request):
    pass




