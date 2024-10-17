from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name= None
    last_name = None
    username = models.CharField(max_length=20, blank=True, null=True)
    fullname = models.CharField(max_length=50)
    id = models.CharField(max_length=75, primary_key=True, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    is_verified = models.BooleanField(default=False)
    OTP = models.IntegerField(max_length=6, blank=True, null=True)
    OTP_VALID_TILL= models.DateTimeField(blank=True, null=True)
    isSuspended = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'username']

    def __str__(self):
        return self.fullname
    