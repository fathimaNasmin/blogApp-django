from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm

from .models import User,Profile
from django.http import JsonResponse

from . import forms

from .utils import custom_register_mail

from django.core.mail import send_mail
from django.core.mail.backends.console import EmailBackend
from django.conf import settings


def signup(request):
    form = forms.SignUpForm(request.POST or None)
    if form.is_valid():
        # form.save()
        user_email = form.cleaned_data['email']
        messages.success(request, 'Account created successfully')
        custom_register_mail(
            subject='Blog App - Account creation',
            message='This is mail to inform that a new account has been created in blog website.You can enjoy our service',
            mail_to=[user_email],
        )
        return redirect('user:signup')
    return render(request, 'user/signup.html', {'form': form})


def login_user(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = forms.LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post:home')

            messages.error(request, "User doesn't exists")
            return redirect('user:login')
    # else:
    #     form = forms.LoginForm()

    return render(request, 'user/login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('post:home')


@login_required
def my_profile(request, pk):
    response = {}
    user = User.objects.get(id=pk)
    u_form = forms.UserUpdateForm(request.POST or None, instance=request.user)
    p_form = forms.ProfileUpdateForm(
                request.POST or None, request.FILES or None)
    if request.method == 'POST':
        try:
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                new_image = request.FILES['profile_image']
                profile_instance = user.profile
                profile_instance.profile_image = new_image
                profile_instance.save()
        except Exception as e:
            response['exception'] = str(e)
            response['status'] = 'danger'
            response['message'] = 'Profile is not updated...Try Again'
        else:
            response['status'] = 'success'
            response['message'] = 'Profile Updated Successfully'

        return JsonResponse(response, safe=False)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'pk': pk,
        'select': 'profile',
    }
    return render(request, 'user/myprofile.html', context)




@login_required
def delete_profile(request, pk):
    if request.method == 'POST':
        # Delete the user's account
        request.user.delete()
        return redirect('post:home')
    return render(request, 'user/delete_my_account.html', {'select': 'delete'})


@login_required
def change_password(request, pk):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('post:home')
        else:
            messages.error(request, 'Password Mismatch')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'user/change_password.html', {
        'form': form,
        'select': 'password'
    })


