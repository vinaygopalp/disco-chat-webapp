from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from chat.models import ChatRoom
from chat.views import finding_all_chatrooms
# Create your views here.

def landing(request):
   return render(request,'index.html')


@login_required
def user_dashboard(request, username):
    if request.user.username == username:
        return render(request, 'users.html')
    else:
        return redirect('login')


def login(request):
    not_matching=False
    if request.method == 'POST':
        not_matching=False
        username = request.POST['username']
        password = request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('login given')
            finding_all_chatrooms(request)
            return HttpResponseRedirect(f'/{username}/login')
        else:
            not_matching=True
            messages.info(request,"Invalid Username")
            
    return render(request,'index.html',{'massage':not_matching})

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    not_matching=False
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        user_name = request.POST['username']
        password1=request.POST['password1']
        ob=User.objects.get(username=user_name)
        if ob:
            messages.info(request,"Username already taken")
            not_matching="not_matching"
        elif password == password1:   
        # Creating a new user
            user = User.objects.create_user(username=user_name , password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.success(request,"Account created successfully")
            print("User created successfully")
            user=auth.authenticate(username=user_name,password=password)
            auth.login(request,user)
        else:
            messages.info(request,"password not matching")
            not_matching="not_matching"  
        # Redirect to home page after successful registration
    return render(request, 'index.html',{'not_matching': not_matching,'username':user_name})