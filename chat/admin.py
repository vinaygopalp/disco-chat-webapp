from django.contrib import admin

# Register your models here.
from chat.models import ChatRoom,Message
# Register your models here.
admin.site.register(ChatRoom)
admin.site.register(Message)