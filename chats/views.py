from django.shortcuts import render
from operator import itemgetter
from itertools import groupby
from django.contrib.auth.decorators import login_required
from chat.models import ChatRoom, Message
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

@login_required
def room(request, room_name):
    chatroom = ChatRoom.objects.filter(code=room_name)
    chatroom_list = []
    all_chats = []

    for chatrooms in chatroom:
        chatroom_list.append(chatrooms.id)

    obj = Message.objects.filter(room_id__in=chatroom_list)
    for j in obj:
        key_base64 = 'X2P3kMgHLqCI83OLFrMHGfSGWovxON5lUUn8K8ERsQ4='
        key = base64.b64decode(key_base64)
        # Encrypted message  
        encrypted_message = j.content   

        try:
            encrypted_bytes = base64.b64decode(encrypted_message)
            backend = default_backend()
            cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
            decryptor = cipher.decryptor()
            decrypted_message = decryptor.update(encrypted_bytes) + decryptor.finalize()
            decrypted_message_str = decrypted_message.decode('utf-8').strip()
        except Exception as e:
            print(f"Decryption error: {e}")
            decrypted_message_str = "Decryption failed"

        current_lst = {
            "sender": str(j.user),
            'message': decrypted_message_str,
            "date": j.timestamp.strftime('%d-%m-%Y'),
            "time": j.timestamp.strftime('%H:%M:%S')
        }
        all_chats.append(current_lst)

    # Sorting by date and time
    all_chats_sorted = sorted(all_chats, key=itemgetter('date', 'time'))

    # Grouping by date
    grouped_chats = {}
    for date, items in groupby(all_chats_sorted, key=itemgetter('date')):
        grouped_chats[date] = list(items)

    return render(request, "users.html", {"room_name": room_name, "grouped_chats": grouped_chats})
