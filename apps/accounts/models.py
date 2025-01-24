from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    ROLL_CHOICE = [
        ('user','User'),
        ('buyer','Buyer'),
        ('vendor','Vendor')
    ]
    role = models.CharField(max_length=15, choices=ROLL_CHOICE, default=False)

    def __str__(self):
        return f"{self.username} ({self.role})"
    
    def is_user(self):
        return self.role == 'user'
    
    def is_buyer(self):
        return self.role == 'buyer'
    

    def is_vendor(self):
        return self.role == 'vendor'

