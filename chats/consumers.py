import json
from channels.generic.websocket import AsyncWebsocketConsumer
from chat.models import Message, ChatRoom
from channels.db import database_sync_to_async
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    @database_sync_to_async
    def my_database_operation(self, encrypted_message, sender):
        room = ChatRoom.objects.get(code=self.room_name, name=sender)
        senderr = User.objects.get(username=sender)
        Message.objects.create(content=encrypted_message, room=room, user=senderr)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print("message:", message)
        sender = text_data_json["sender"]

        await self.my_database_operation(message, sender)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": sender,
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]

        await self.send(text_data=json.dumps({
            "message": message,
            "sender": sender,
        }))
