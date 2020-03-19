from django.urls import path
from . import views
#from users import views as user_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logins/', views.loginpage, name='logins'),
    # path('logout/', views.logout, name='logout'),
  
]