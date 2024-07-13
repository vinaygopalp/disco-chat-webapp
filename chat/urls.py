from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
    # path('',views.first,name='chat'),
     path('login/create-chat-room/', views.create_chat_room, name='create_chat_room'),
      path("addmember", views.addmember, name="addmember"),
      path("<str:room_name>/delete", views.room_delete, name="room_delete"),
     ]

