from django.shortcuts import render
from enroll.models import Problem

def probleminfo(request):
    prob = Problem.objects.all()
    return render(request,'problemdetails1.html',{'pro': prob})

def submit(request):
    return render(request,'submit_sol.html')
