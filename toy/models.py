from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tuy(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Name=models.CharField( max_length=50)
    Firstname=models.CharField( max_length=50)
    Lastname=models.CharField( max_length=50)
    Age=models.IntegerField()