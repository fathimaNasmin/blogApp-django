from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm

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

            print('Invalid username or password')
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
    if request.method == 'POST':
        try:
            u_form = forms.UserUpdateForm(request.POST, instance=request.user)
            p_form = forms.ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, 'Profile Updated Successfully')
            return redirect('user:my-profile', {'pk': request.user.id})
        except Exception as e:
            print(e)

    else:
        u_form = forms.UserUpdateForm(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.profile)

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

# TODO : display the profile picture
# TODO : forgot password?
# TODO: Social authentication
# TODO: static file-aws s3
#TODO: hide the secret key's before deploying

# username:admin; password: legacy0711