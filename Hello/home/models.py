from django.db import models
from Hello.settings import BASE_DIR
from django.contrib.auth.models import User
import os



class Problem(models.Model):
    prob_id=models.IntegerField(primary_key=True)
    prob_name=models.CharField(max_length=100)
    prob_link=models.FilePathField(path=BASE_DIR/'static')
    test_input=models.FilePathField(path=BASE_DIR/'TEST-INPUT')
    test_output=models.FilePathField(path=BASE_DIR/'TEST-OUTPUT')
    editorial=models.CharField(default='#',max_length=100)


class Solution(models.Model):
    sol_id=models.IntegerField(primary_key=True)
    prob_id=models.ForeignKey(Problem,on_delete=models.DO_NOTHING)
    sol_link=models.ForeignKey(User,on_delete=models.DO_NOTHING)  #doubt
    test_input=models.FilePathField(path=BASE_DIR/'TEST-INPUT')
    test_output=models.FilePathField(path=BASE_DIR/'TEST-OUTPUT') #doubt_generated_file?
    vis_id=models.IntegerField()

class Visitor(models.Model):
    vis_name=models.CharField(max_length=100)
    vis_email = models.CharField(max_length=100)
    vis_password= models.CharField(max_length=100)
    #vis_last_login=models.TimeField(default =None)
    vis_problem_attempted=models.IntegerField(default=0)
    vis_problem_solved=models.IntegerField(default=0) #attempted
    vis_problem_list =models.CharField(max_length=500) #name of problems solved by user




