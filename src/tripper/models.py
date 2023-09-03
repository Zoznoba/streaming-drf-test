from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=50)
    surname = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    
    