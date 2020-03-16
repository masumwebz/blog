from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'Masum',
        'title': 'Blog Post',
        'content': 'First Content dolor sit amet, consectetg elit, sed do eiusmod tempor incididunt ut labore.',
        'date_posted': 'Jul 3 1987',
    },
    {
        'author': 'newuser',
        'title': 'New Post',
        'content': 'Second Content dolor sit amet, elit, sed do eiusmod tempor incididunt ut labore.',
        'date_posted': 'aug 3 1987',
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

