from django.urls import path
from . import views
#from users import views as user_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('task/', views.task, name='task-list'),
    path('album/', views.album, name='album-list'),
    #path('register', user_views.register, name='register'),
]