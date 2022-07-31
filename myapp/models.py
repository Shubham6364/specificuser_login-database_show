from django.db import models
from django.contrib.auth.models import User , auth
# Create your models here.


class specific(models.Model):
	fname = models.CharField(max_length=200,null=True)
	sname = models.CharField(max_length=300,null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)  # new




class signup(models.Model):
	email = models.EmailField(max_length=200,null=True)
	password = models.CharField(max_length=200,null=True)
	repeatpassword =  models.CharField(max_length=200,null=True)





