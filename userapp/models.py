from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username
