from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import CustomerForm, CreateUserForm

from .decorators import unauthenticated_user, allowed_users
from django.contrib import messages


# Logs a user in
@unauthenticated_user
def login_user(request):
  if request.method =='POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
      
    print(username)  
    user = authenticate(request, username=username, password=password)
    print(user)
      
    if user is not None:
      login(request, user)
      print(username, 'logged in')
      return redirect('market:home')
      
    else: messages.error(request, 'Account not Registered')
  return render(request, 'user/login.html')


# Registers a new user
@unauthenticated_user
def register(request):
  form = CreateUserForm()
    
  if request.method=='POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      
      
      messages.success(request," Account was Created for "+username)
      return redirect('user:login')
    else:
      messages.error(request, 'Incorrect credentials')
        
  context = {'form':form}
  return render(request,'user/register.html', context)