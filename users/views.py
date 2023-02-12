from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, ProfileForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic.edit import DeleteView
from django.db.models import Q
from .utils import searchProfiles, paginateProfiles

from .models import Profile
from . import views


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    projects = profile.project_set.all()
    context = {
        'profile':profile,
        'projects':projects,
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccountView(request):
    model = Profile
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)




@login_required
def deleteAccountView(request, pk, *args, **kwargs):
    model = Profile
    # profile = request.user.profile
    profile = User.objects.get(id=pk)
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    template_name = 'projects/delete_template.html'
    
    if request.method == "POST":
        # profile = Profile.objects.get(id=pk)
        profile.is_active = False
        profile.save()
        
        messages.success(request, 'Profile deleted successfully')
        return HttpResponseRedirect(reverse_lazy('register'))
    
    context = {
        'model':model,
        'profile':profile,
        'template_name':template_name,
    }

    return render(request, 'projects/delete_template.html', context)
    


def profiles(request):
    profiles, search_query = searchProfiles(request)
    custom_range, profiles = paginateProfiles(request, profiles, 3)
    context = {
        'profiles': profiles,
        'search_query': search_query,
        'custom_range': custom_range,
        }
    return render(request, 'users/profiles.html', context)



def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {
        'profile': profile,
        }
    return render(request, 'users/user-profile.html', context)




def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'User was successfully logged out')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('account')

        else:
            messages.error(request, 'An error has occurred during registration!')

    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)

