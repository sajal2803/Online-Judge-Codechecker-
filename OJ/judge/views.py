from asyncio.windows_events import NULL
from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from judge.models import Problem, Visitor ,Submission

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
 
  
def signin(request):
   username =NULL
   if request.method == 'POST':
       username = request.POST['username']
       pass1 = request.POST['pass1']
      
       user=Visitor.objects.filter(username=username, password=pass1)
      
       if len(user) > 0:
           
           messages.success(request, "Logged In Sucessfully!!")
           return render(request, "index.html",{"user":user[0]})
       else:
           messages.error(request, "Bad Credentials!!")
           return redirect('home')
  
   return render(request, "signin.html") #signin.html -->pas user
 
 
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


def probleminfo(request,username):
    prob =Problem.objects.all()
    user=Visitor.objects.get(username=username)
    return render(request,'problemdetails.html',{'pro':prob,'vis':user})

def problem_description(request,username,prob_id):
   
    user = Visitor.objects.get(username=str(username))
    id = Problem.objects.get(id=prob_id)
    #rank = Visitor.objects.all().filter(problems_solved__gt=user.problems_solved).count() + 1
    return render(request,'problem_description.html',{'ID':id,'user':user})

def submit(request, username, prob_id):
    if request.method == "POST":
       username = username
       prob_id = prob_id
       code = request.POST['usercode']
       code =str(code)
       textfile = open("solution.py", "w")
       textfile.write(code)
       textfile.close()