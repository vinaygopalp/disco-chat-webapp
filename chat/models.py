from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User,auth
import random
import string

def generate_unique_key():
    # Generate a random 6-character alphanumeric key (uppercase letters + digits)
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class ChatRoom(models.Model):
    code = models.CharField(max_length=6,editable=False)
    name = models.CharField(max_length=255,default=User)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chatrooms', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.content[:20]}'
