from django.shortcuts import render, redirect
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
#from .forms import CreateUserForm
from .forms import *
# Create your views here.

#@login_required(login_url='login')
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)

def task(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('task-list')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)


def register(request):
    form = UserCreationForm()
    return render (request, 'blog/register.html', {'form':form})




#album views
def album(request):
    album = Album.objects.all()
    form = AlbumForm()

    if request.method =='POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            # album= form.save(commit=False)
            # album.artist = request.user
            # form.save()
            instance = form.save(commit=False)
            instance.artist = request.user
            instance.save()

        return redirect('album-list')

    context = {'album':album, 'form':form}
    return render(request, 'tasks/album.html', context)