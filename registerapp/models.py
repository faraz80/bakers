from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
    user_n = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    
    #def __str__(self):
    #    return self.user_n
    