from django.urls import path
from . import views
#from users import views as user_views

urlpatterns = [
    path('register/', views.register, name='register'),
     path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
  
]