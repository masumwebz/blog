from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


#register views
def register(request):
    if request.user.is_authenticated:
        return redirect('blog-home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account successfully created for ' + user )
                return redirect('register')

        context = { 'form':form }
        return render(request, 'users/register.html', context)





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