from django.shortcuts import render , HttpResponse
from home.models import Problem, Solution
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'variable':"this is sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")

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

