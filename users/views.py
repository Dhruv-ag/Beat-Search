# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from allauth.socialaccount.models import SocialAccount
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created, You are now able to login');
            return redirect('login')

    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
def pics(request):
    try:
        ed=SocialAccount.objects.get(user=request.user).extra_data.get('picture')
        return render(request,'users/profile.html',{'ed':ed})
    except:
        try:
            ed = User.objects.get(username=request.user.username).profile.image.url
            return render(request,'users/profile.html',{'ed':ed})
        except:
            ed='/home/dhruv/Desktop/Codes/Webd/songsapi/songs_project/songs_app/templates/default.jpeg'
            return render(request,'users/profile.html',{'ed':ed})


@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated');
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
    'u_form':u_form,
    'p_form':p_form
    }
    return render(request,'users/profile.html',context)
