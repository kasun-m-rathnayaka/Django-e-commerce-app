from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegister
from store.models import User

def register_user(request):
    if request.method == 'POST':
        form = UserRegister(request.POST, request.FILES)
        if form.is_valid():

            return redirect('success')
        else:
            return render(request, 'user/register.html', {'form': form})
    else:
        form = UserRegister()
    return render(request, 'user/register.html', {'form': form, 'message': 'Please upload a file'})


def login(request):
    return render(request, 'user/login.html', {})