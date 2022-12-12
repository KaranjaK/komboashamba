from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='singup'),
    path('signin', views.signin, name='singin'),
    path('signout', views.signout, name='singout'),
]