from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


# #register views
# def register(request):
#     if request.user.is_authenticated:
#         return redirect('blog-home')
#     else:
#         form = CreateUserForm()
#         profileform = UserProfileForm()
#         if request.method == 'POST':
#             form = CreateUserForm(request.POST)
#             profileform = UserProfileForm(request.POST)
#             if form.is_valid() and profileform.is_valid():
#                 form.save()

#                 profile = profileform.save(commit=False)
#                 profile.user = user
#                 profile.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Account successfully created for ' + user )
#                 return redirect('register')

#         context = { 'form':form, 'profileform': profileform }
#         return render(request, 'users/register.html', context)



#register views
def register(request):

    if request.method == 'POST':
        form = ExtendUserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('register')
        
    else:
        form = ExtendUserForm()
        profile_form = UserProfileForm()

    context = { 'form':form, 'profile_form':profile_form}
    return render(request,'users/register.html', context)
    






# login page views
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('blog-home')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('blog-home')
            else:
                messages.info(request, 'pass ki vule gesen?')
        context = {}

        return render(request,'users/login.html',context)

#logout views
def logoutuser (request):
    logout(request)
    return redirect('login')