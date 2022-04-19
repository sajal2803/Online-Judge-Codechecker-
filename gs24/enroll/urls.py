from django.urls import path
from . import views

urlpatterns=[
    path('problems/',views.probleminfo),
    path('problems/submit',views.submit),
]