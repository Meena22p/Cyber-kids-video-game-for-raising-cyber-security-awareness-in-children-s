from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_index,name='main_index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('user_login',views.user_login,name='user_login'),
    path('user_register',views.user_register,name='user_register'),
    
]