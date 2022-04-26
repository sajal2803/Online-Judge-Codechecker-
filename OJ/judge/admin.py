from django.contrib import admin

from judge.models import Problem, Submission, Visitor

# Register your models here.

admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(Visitor)
