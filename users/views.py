# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate,logout as auth_logout
from .forms import UserRegisterForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.warning(request, f'User {username} is already registered!')
                return redirect('login')
            form.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'users/login.html')
def home(request):
    if request.user.is_authenticated:
        return render(request,'users/home.html')
    else:
        return redirect('register')
    
def logout(request):
    auth_logout(request)
    messages.success(request,'YOU HAVE BEEN SUCCESSFULLY LOGGED OUT!!')
    return redirect('login')
