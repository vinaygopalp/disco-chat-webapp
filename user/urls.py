
from django.contrib import admin
from django.urls import path
from . import views
from chat.views import create_chat_room as create_chat_room
urlpatterns = [
   
    path('',views.landing,name='landing'),
    # path('user',views.user,name='user'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),

    path('<str:username>/login', views.user_dashboard, name='user_dashboard'),  # New route for user dashboard
    # other url patterns
 ]