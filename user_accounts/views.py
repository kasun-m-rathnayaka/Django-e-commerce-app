from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegister
from store.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def register_user(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['f_name'],
                last_name=form.cleaned_data['l_name'],
            )
            messages.success(request, 'Registration successful')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('storehome')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'user/login.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('storehome')