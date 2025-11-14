from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user_dashboard',views.user_dashboard,name='user_dashboard'),
    path('user_feedback',views.user_feedback,name='user_feedback'),
    path('games',views.games,name='games'),
    path('questions/<int:id>/',views.questions,name='question'),
    path('play_game/<int:id>/',views.play_game,name="play_game"),
    path('logout',views.logout,name='logout')
]