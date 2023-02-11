from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . import forms


# TODO: write test.py

def signup(request):
    form = forms.SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("form is valid")
        print('Account created successfully')
        messages.success(request, 'Account created successfully')
        return redirect('user:signup')
    return render(request, 'user/signup.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post:home')
            else:
                print('Invalid username or password')
                return render(request, 'user/login.html', {'error': 'Invalid login credentials'})
    else:
        form = forms.LoginForm()

    return render(request, 'user/login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('post:home')
