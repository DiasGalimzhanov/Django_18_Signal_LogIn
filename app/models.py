from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_pictures', null=True, blank=True, default='default.jpg') 
    birthday = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=12)   
    
    def __str__(self):
        return self.username
    
    