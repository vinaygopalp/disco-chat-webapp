from django.shortcuts import render
from operator import itemgetter
from itertools import groupby
from django.contrib.auth.decorators import login_required
from chat.models import ChatRoom, Message
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii
  
key = '8809a0e4ccd1cf0dfcbbc4de3ca6f9b4'

# def decrypt_message_cbc(encrypted_message, key):
#     # Convert the encrypted message from hex to bytes
#     encrypted_bytes = binascii.unhexlify(encrypted_message)
    
#     # Extract the IV (first 16 bytes) and ciphertext (rest of the bytes)
#     iv = encrypted_bytes[:16]
#     ciphertext = encrypted_bytes[16:]
    
#     # Create an AES cipher object with the key and extracted IV in CBC mode
#     cipher = AES.new(key, AES.MODE_CBC, iv)
    
#     # Decrypt the ciphertext
#     decrypted_padded_message = cipher.decrypt(ciphertext)
    
#     # Unpad the decrypted message and return it as a UTF-8 string
#     return unpad(decrypted_padded_message, AES.block_size).decode('utf-8')


def decrypt_message_cbc(encrypted_message, key):
    try:
        # Convert the encrypted message from hex to bytes
        encrypted_bytes = binascii.unhexlify(encrypted_message)
        
        # Extract the IV (first 16 bytes) and ciphertext (rest of the bytes)
        iv = encrypted_bytes[:16]
        ciphertext = encrypted_bytes[16:]
        
        # Create an AES cipher object with the key and extracted IV in CBC mode
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        
        # Decrypt the ciphertext
        decrypted_padded_message = cipher.decrypt(ciphertext)
        
        # Unpad the decrypted message and return it as a UTF-8 string
        return unpad(decrypted_padded_message, AES.block_size).decode('utf-8')

    except Exception as e:
        print(f"Decryption error: {e}")
        return "Decryption failed"
    try:
       
    # Generate a random 16-byte IV (Initialization Vector)
        iv = get_random_bytes(16)
        print("incrpyted:",message)
        # Create an AES cipher object with the key and IV in CBC mode
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        
        # Pad the message to be a multiple of AES block size (16 bytes)
        padded_message = pad(message.encode('utf-8'), AES.block_size)
        
        # Encrypt the padded message
        ciphertext = cipher.encrypt(padded_message)
        print()
        # Return the IV and ciphertext concatenated together (both in hexadecimal format)
        return binascii.hexlify(iv + ciphertext).decode('utf-8')

    except base64.binascii.Error as e:
        print(f"Base64 error: {e}")
        return "Decryption failed due to format error"
    except ValueError as e:
        print(f"Padding error: {e}")
        return "Decryption failed due to padding error"
    except Exception as e:
        print(f"Decryption error: {e}")
        return "Decryption failed"
@login_required
def room(request, room_name):
    chatroom = ChatRoom.objects.filter(code=room_name)
    chatroom_list = []
    all_chats = []

    for chatrooms in chatroom:
        chatroom_list.append(chatrooms.id)

    obj = Message.objects.filter(room_id__in=chatroom_list)
    for j in obj:
        # key_base64 = 'X2P3kMgHLqCI83OLFrMHGfSGWovxON5lUUn8K8ERsQ4='
        # key = base64.b64decode(key_base64)
        # Encrypted message  
        encrypted_message = j.content   

        # try:
        #     encrypted_bytes = base64.b64decode(encrypted_message)
        #     backend = default_backend()
        #     cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
        #     decryptor = cipher.decryptor()
        #     decrypted_message = decryptor.update(encrypted_bytes) + decryptor.finalize()
        #     decrypted_message_str = decrypted_message.decode('utf-8').strip()
        # except Exception as e:
        #     print(f"Decryption error: {e}")
        #     decrypted_message_str = "Decryption failed"
        decrypted_message_str=decrypt_message_cbc(encrypted_message, key)
        current_lst = {
            "sender": str(j.user),
            'message': decrypted_message_str,
            "dates": j.timestamp.strftime('%Y-%m-%d'),
            "date": j.timestamp.strftime('%d-%m-%Y'),
            "time": j.timestamp.strftime('%H:%M:%S')
        }
        all_chats.append(current_lst)

    # Sorting by date and time
    all_chats_sorted = sorted(all_chats, key=itemgetter('dates', 'time'))

    # Grouping by date
    grouped_chats = {}
    for date, items in groupby(all_chats_sorted, key=itemgetter('date')):
        grouped_chats[date] = list(items)
    print(grouped_chats)
    return render(request, "users.html", {"room_name": room_name, "grouped_chats": grouped_chats})
