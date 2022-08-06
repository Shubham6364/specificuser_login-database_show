from django.db import models

# Create your models here.


class Specific(models.Model):
	fname = models.CharField(max_length=200,null=True)
	sname = models.CharField(max_length=300,null=True)
	usernanme = models.ForeignKey('Signup', on_delete=models.CASCADE,null=True)  # new

	def __str__(self):
		return self.username




class Signup(models.Model):
	username = models.CharField(max_length=200,null=True)
	password = models.CharField(max_length=200,null=True)
	


class Adminsignup(models.Model):
	uname= models.CharField(max_length=200,null=True)
	pwd = models.CharField(max_length=200,null=True)






