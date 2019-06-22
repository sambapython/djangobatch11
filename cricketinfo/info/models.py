from django.db import models

# Create your models here.
class Country(models.Model):
	name=models.CharField(max_length=250, unique=True)
	flag=models.ImageField(blank=True, null=True)
	shortname = models.CharField(max_length=256, unique=True)
	#description=models.TextField(max_length=500,blank=True, null=True)
	description=models.TextField(max_length=555,default="about your country")

	def __str__(self):
		return self.name
def dob_validate(dob_date):
	print("*"*20)
	print(dob_date)
class Player(models.Model):
	specials = [("bm","BATS MAN"),("bl","BOWLER"),("kr","KEEPER"),("ar","ALL ROUNDER")]
	name=models.CharField(max_length=250)
	dob = models.DateField(validators=[dob_validate])
	special = models.CharField(choices=specials, max_length=3)
	country = models.ForeignKey(Country,on_delete=models.PROTECT)
	active = models.BooleanField(default=True)

class Country1(models.Model):
	name=models.CharField(max_length=250, unique=True, primary_key=True)
	flag=models.ImageField(blank=True, null=True)
	shortname = models.CharField(max_length=256, unique=True)
	#description=models.TextField(max_length=500,blank=True, null=True)
	description=models.TextField(max_length=555,default="about your country")
