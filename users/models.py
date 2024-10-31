from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    username = models.CharField(max_length=50, unique=True)
    nickname = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
