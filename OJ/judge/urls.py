from django.contrib import admin
from django.urls import path ,include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('home/',views.home, name='home'),
    path('problems/<username>/', views.probleminfo),
    path('problems/<username>/<int:prob_id>/', views.problem_description , name='problem_description'),
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('submit/<username>/<int:prob_id>/',views.submit,name='submit')
    #url(r'^emp_detail/(?P<user_name>\w+)/(?P<mobile_number>\d{10,18})/$', views.emp_detail, name='emp_detail'),
]