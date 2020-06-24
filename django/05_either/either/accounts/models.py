from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): #CustomUser임. 기존의 User를 이 User로 대체함
    phone = models.CharField(max_length=20)