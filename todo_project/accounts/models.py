from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields here
    username=models.CharField(max_length = 200, unique=True)
    email=models.CharField(max_length = 200)
    first_name=models.CharField(max_length = 200)
    last_name=models.CharField(max_length = 200)
    bio = models.TextField(blank=True, null=True)
    is_staff=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title