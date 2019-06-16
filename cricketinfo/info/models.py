from django.db import models

# Create your models here.
class Country(models.Model):
	name=models.CharField(max_length=250, unique=True)
	flag=models.ImageField(blank=True, null=True)
	shortname = models.CharField(max_length=256, unique=True)
	#description=models.TextField(max_length=500,blank=True, null=True)
	description=models.TextField(max_length=555,default="about your country")

	

class Country1(models.Model):
	name=models.CharField(max_length=250, unique=True, primary_key=True)
	flag=models.ImageField(blank=True, null=True)
	shortname = models.CharField(max_length=256, unique=True)
	#description=models.TextField(max_length=500,blank=True, null=True)
	description=models.TextField(max_length=555,default="about your country")
