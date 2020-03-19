from django.shortcuts import render, redirect
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
#from .forms import CreateUserForm
from .forms import *
# Create your views here.


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
    albums = Album.objects.all()
    form = AlbumForm()

    if request.method =='POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
           # albums.artist = request.user
            form.save()
        return redirect('album-list')

    context = {'albums':albums, 'form':form}
    return render(request, 'tasks/album.html', context)