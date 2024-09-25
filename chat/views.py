from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import ChatRoom
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User,auth
# Create your views here.
import random
import string
import google.generativeai as genai
from django.http import JsonResponse
import json
 
@login_required
def finding_all_chatrooms(request):
    username=request.user.username
    chat_rooms = ChatRoom.objects.filter(name=username)
    chat_room_codes = chat_rooms.values('pk','code')
    chat_room_codes_list = list(chat_room_codes)
   
    # Store chat room codes in session to use in the redirected view
    request.session['chat_room_codes'] = chat_room_codes_list

def generate_unique_key():
    # Generate a random 6-character alphanumeric key (uppercase letters + digits)
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def unique():
    code=generate_unique_key()
    obj=ChatRoom.objects.filter(code=code)
    if obj.exists():
        return unique()
    else:    
        return code

@login_required
def create_chat_room(request):
        code=unique()
        user = request.user.username
        print(user)
        chat_room = ChatRoom.objects.create(name=user,code=code)
        chat_room.save()
        finding_all_chatrooms(request)
        return HttpResponseRedirect(f'/{request.user.username}/login')

@login_required
def room_delete(request,room_name):
    chat_room = ChatRoom.objects.get(name=request.user.username,code=room_name)
    print(chat_room)
    chat_room.delete()
    finding_all_chatrooms(request)
    return redirect(f'/{request.user.username}/login')

def addmember(request):
    if request.method == 'POST':
        user = request.user.username
        code=request.POST['code']
       
        try:
            obj = ChatRoom.objects.get(code=code, name=user)
            return HttpResponseRedirect(f'/chat/{code}')
        except ChatRoom.DoesNotExist:
            chat_room = ChatRoom.objects.create(name=user, code=code)
            chat_room.save()
            finding_all_chatrooms(request)
            return redirect(f'/{request.user.username}/login')


@login_required
def chat_room_detail(request, room_code):
    chat_room = ChatRoom.objects.get(code=room_code)
    return render(request, 'chat_room.html', {'chat_room': chat_room})


@login_required
def all_chatroom(request):
    username=request.user.username
    
    obj=ChatRoom.objects.filter(name=username)
    # return HttpResponseRedirect(f'/{username}/login',{'list_obj':obj})
@login_required
def ai_chatting(request,username):
    ai=True
    if request.method == 'POST':
        data = json.loads(request.body)
        
        message = data.get('message', '')
   
        genai.configure(api_key='' )
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(message)
       
        # Return the processed data back to the frontend
        response_data = {
            'status': 'success',
            'response_message': response.text,
        }
        return JsonResponse(response_data)
        

    return render(request,'users.html',{'ai':ai})
