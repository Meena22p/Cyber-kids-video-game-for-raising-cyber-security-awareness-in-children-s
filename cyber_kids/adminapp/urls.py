from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('add_game',views.add_game,name='add_game'),
    path('manage_games',views.manage_games,name='manage_games'),
    path('delete_game/<int:id>/',views.delete_game,name='delete_game'),
    path('edit_game/<int:id>/',views.edit_game,name='edit_game'),
    path('add_questions',views.add_questions,name='add_questions'),
    path('manage_questions/',views.manage_questions,name='manage_questions'),
    path('edit_questions/<int:id>/',views.edit_question,name='edit_questions'),
    path('delete_questions/<int:id>/',views.delete_question,name='delete_question'),


    path('user_details',views.user_details,name='user_details'),
    path('delete_user/<int:id>/',views.user_delete,name='user_delete'),
    path('cyber_kids_analysis',views.cyber_kids_analysis,name='cyber_kids_analysis'),
    path('feedback_management',views.feedback_management,name='feedback_management'),
    path('admin-logout/',views.admin_logout,name="admin_logout"),
]