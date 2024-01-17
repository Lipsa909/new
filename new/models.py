from django.db import models
from django.contrib.auth.models  import User


# Create your models here.

class skj(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Name=models.CharField( max_length=50)
    FirstName=models.CharField( max_length=50)
    LastName=models.CharField( max_length=50)
    Age=models.IntegerField()


    
    
        
    
    