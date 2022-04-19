from django.db import models
from gs24.settings import BASE_DIR
from django.contrib.auth.models import User
import os



class Problem(models.Model):
    prob_id=models.IntegerField(primary_key=True)
    prob_name=models.CharField(max_length=100)
    prob_link=models.FilePathField(path=BASE_DIR/'static')
    test_input=models.FilePathField(path=BASE_DIR/'TEST-INPUT')
    test_output=models.FilePathField(path=BASE_DIR/'TEST-OUTPUT')


class Solution(models.Model):
    sol_id=models.IntegerField(primary_key=True)
    prob_id=models.ForeignKey(Problem,on_delete=models.DO_NOTHING)
    sol_link=models.ForeignKey(User,on_delete=models.DO_NOTHING)  #doubt
    test_input=models.FilePathField(path=BASE_DIR/'TEST-INPUT')
    test_output=models.FilePathField(path=BASE_DIR/'TEST-OUTPUT') #doubt_generated_file?
    user_id=models.IntegerField()