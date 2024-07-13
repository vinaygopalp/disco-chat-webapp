from django.db import models
from django.conf import settings
import random
import string

def generate_unique_key():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class ChatRoom(models.Model):
    code = models.CharField(max_length=6, unique=True, editable=False)
    name = models.CharField(max_length=255, default='')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chatrooms', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_key()
            while ChatRoom.objects.filter(code=self.code).exists():
                self.code = generate_unique_key()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.content[:20]}'
