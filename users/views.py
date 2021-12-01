from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from feed.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import Profile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import random

User = get_user_model()

##This will simply display all of the users...

def user_list(request):
    users = Profile.objects

    return render(request, "users/user_list.html", {'users': users})

def follow(request, id):
    #The user is the person you want to follow
    user1 = get_object_or_404(User, id = id )

    #the user2 represents your profile
    user2 = request.user.profile

    ## Add the persons profile you want to follow to your acct
    user2.profile.following.add(user1.profile)

    ##Add your profile to the person you followed folllowers list...
    user1.profile.followers.add(user2.profile)

    ## redirect to your profile?

    return HttpResponseRedirect('/users') 

#Look at your followers
def view_followers(request):
    u = request.user.profile

    followers = u.followers

    return render(request, 'users/followers.html', {'followers':followers})

def profile_view(request, slug):
    p = Profile.objects.filter(slug = slug).first()
    u = p.user

    context = {
        'user' : u
    }

    #Sends user info to the profile...
    return render(request, 'users/profile.html', context) 

def my_profile(request):
    p = request.user.profile
    u = p.user

    context = {
        'user' : u
    }

    #Sends user info to the profile...
    return render(request, 'users/profile.html', context) 


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You can now login!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('my_profile')
    else: 
        form = ProfileUpdateForm(instance = request.user)
    return render(request, 'users/edit_profile.html', {'form': form})
    ##allow users to edit their profiles...








