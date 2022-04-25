from django.db import models
from Hello.settings import BASE_DIR
from django.contrib.auth.models import User
import os


class Visitor(models.Model):
    username= models.CharField(primary_key=True , max_length= 100)
    name= models.CharField(max_length=100)
    email = models.CharField(unique=True,max_length=100)
    password = models.CharField(max_length=100)
    problem_solved= models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class Problem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 100)
    type = models.CharField(max_length= 100)
    difficulty = models.CharField(max_length= 100)
    statement=models.TextField()
    task=models.TextField(null=True)
    time_complexity=models.CharField(max_length=50,null =True)
    space_complexity=models.CharField(max_length=50,null =True)
    constraints=models.CharField(max_length=50,null =True)
    example=models.TextField(null =True)

    def __str__(self) -> str:
        return self.name

class Submission(models.Model):
    visitor = models.ForeignKey(Visitor,on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    verdict = models.CharField(max_length=100)
    time =models.DateTimeField()

class TestCases(models.Model):
    input = models.TextField()
    output = models.TextField()
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE,null=True)

    
    


