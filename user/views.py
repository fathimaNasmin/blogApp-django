import os
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm

from .models import User, Profile
from django.http import JsonResponse

from . import forms

from user.signals import user_profile_updated


def signup(request):
    form = forms.SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        user_email = form.cleaned_data['email']
        messages.success(request, 'Account created successfully')
        return redirect('user:signup')
    return render(request, 'user/signup.html', {'form': form})


def login_user(request):
    next_url = ''
    form = forms.LoginForm()
    if request.method == "POST":
        
        form = forms.LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if next_url:
                    return redirect(next_url)
                return redirect("post:home")

            messages.error(request, "User doesn't exists")
            return redirect('user:login')
    else:
        print(request.GET)
        next_url = request.GET.get("next", "post:home")
        print(next_url)

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
                
                if request.FILES.get('profile_image'):
                    new_image = request.FILES['profile_image']
                    try:
                        # Check if the original file exists
                        if user.profile.profile_image and os.path.exists(user.profile.profile_image.path):
                            # File exists, update it
                            user.profile.profile_image = new_image
                            user.profile.save()
                        else:
                            # Delete the existing profile instance
                            try:
                                if user.profile:
                                    user.profile.delete()
                                    print("Deleted existing profile instance")
                            except Exception as e:
                                print(
                                    f"Error deleting existing profile instance: {e}")

                            # Create a new profile instance with the new image
                            try:
                                new_profile_instance = Profile.objects.create(
                                    user=user, profile_image=new_image)
                                print("Created new profile instance")
                            except Exception as e:
                                print("Error creating a new profile instance:", e)
                    except Exception as e:
                        print("profile:",e)
                
                # Emit the signal to send mail to the user on user updation
                try:
                    user_profile_updated.send(sender=User, instance=user)
                except Exception as signal_exception:
                    print("signal_exception:",signal_exception)
                else:
                    print("mail send")
            else:
                print("form is not valid")
                print("u_form error:",u_form.errors)
                print("p_form error:",p_form.errors)
        except Exception as e:
            print(e)
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


