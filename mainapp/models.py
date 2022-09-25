from http.cookiejar import Cookie
from pyexpat import model
from xml.dom.minidom import Element
from django.db import models
from django.contrib.auth.models import User

# from djongo import models

# Create your models here.

class Tags(models.Model):
    # tag_id=models.AutoField(primary_key=True)
    section=models.CharField(max_length=100,primary_key=True)
    
# setup()
class Elements(models.Model):
    elementid = models.AutoField(primary_key=True)
    name_grms=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    price=models.CharField(max_length=100)
    typee= models.ForeignKey(Tags,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name_grms
    # type=models.CharField(max_length=100,choices=get())

class purchases(models.Model):
    user_n = models.ForeignKey(User,on_delete=models.CASCADE)
    bill_no= models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    total=models.IntegerField()
    def __str__(self):
        return self.product_name


