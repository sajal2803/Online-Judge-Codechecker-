from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
from home.models import Problem, Visitor

# Create your views here.
def index(request):
    context={
        'variable':"this is sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")
def signup(request):
   if request.method == "POST":
       username = request.POST['username']
       fname = request.POST['fname']
       lname = request.POST['lname']
       email = request.POST['email']
       pass1 = request.POST['pass1']
       pass2 = request.POST['pass2']
      
       if Visitor.objects.filter(username=username).exists():
           messages.error(request, "Username already exist! Please try some other username.")
           return redirect('home')
      
       if Visitor.objects.filter(email=email).exists():
           messages.error(request, "Email Already Registered!!")
           return redirect('home')
      
       if len(username)>20:
           messages.error(request, "Username must be under 20 charcters!!")
           return redirect('home')
      
       if pass1 != pass2:
           messages.error(request, "Passwords didn't matched!!")
           return redirect('home')
      
       visitor=Visitor(username=username,name=fname+lname,email=email,password=pass1)
       visitor.save()
       messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
       return redirect('signin')
      
   else:   
     return render(request, "signup.html")
 
 
def activate(request,uidb64,token):
   try:
       uid = force_text(urlsafe_base64_decode(uidb64))
       myuser = User.objects.get(pk=uid)
   except (TypeError,ValueError,OverflowError,User.DoesNotExist):
       myuser = None
 
   if myuser is not None and generate_token.check_token(myuser,token):
       myuser.is_active = True
       # user.profile.signup_confirmation = True
       myuser.save()
       login(request,myuser)
       messages.success(request, "Your Account has been activated!!")
       return redirect('signin')
  
def signin(request):
   if request.method == 'POST':
       username = request.POST['username']
       pass1 = request.POST['pass1']
      
       user = authenticate(username=username, password=pass1)
      
       if user is not None:
           login(request, user)
           fname = user.first_name
           # messages.success(request, "Logged In Sucessfully!!")
           return render(request, "index.html",{"fname":fname})
       else:
           messages.error(request, "Bad Credentials!!")
           return redirect('home')
  
   return render(request, "signin.html") #signin.html
 
 
def signout(request):
   logout(request)
   messages.success(request, "Logged Out Successfully!!")
   return redirect('home')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
def home(request):
     return render(request, 'home.html')

def submit(request):
    return render(request,'submit_sol.html')
def probleminfo(request):
    prob =Problem.objects.all()
    return render(request,'problemdetails1.html',{'pro':prob})

