from django.contrib import admin
from django.urls import path ,include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('home/',views.home, name='home'),
    path('problems/', views.probleminfo),
    path('problems/submit', views.submit , name='submit'),
    path('signup',views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('activate/<uidb64>/<token>', views.activate ,name='activate'),


]