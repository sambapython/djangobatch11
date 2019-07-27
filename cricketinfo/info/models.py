from django.db import models
from django.contrib.auth.models import AbstractUser
class abst(models.Model): # abstract model
	name=models.CharField(max_length=250)
	class Meta:
		abstract=True
class Country(abst):
	#name=models.CharField(max_length=250, unique=True)
	flag=models.ImageField(blank=True, null=True)
	shortname = models.CharField(max_length=256, unique=True)
	#description=models.TextField(max_length=500,blank=True, null=True)
	description=models.TextField(max_length=555,default="about your country")

	def __str__(self):
		return self.name

class UserProfile(AbstractUser):
	country = models.ForeignKey(Country,on_delete=models.PROTECT,
		related_name="userprofile",null=True,blank=True)
	#role = models.CharField(choices=[(""),()])

# Create your models here.

def dob_validate(dob_date):
	print("*"*20)
	print(dob_date)
class Player(abst):
	specials = [("bm","BATS MAN"),("bl","BOWLER"),("kr","KEEPER"),("ar","ALL ROUNDER")]
	#name=models.CharField(max_length=250)
	dob = models.DateField(validators=[dob_validate])
	special = models.CharField(choices=specials, max_length=3,)
	country = models.ForeignKey(Country,on_delete=models.PROTECT)
	active = models.BooleanField(default=True)
	pic = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.name
	def get_id(self):
		
		return self.id

class Country1(abst):
	name=models.CharField(max_length=250, unique=True, primary_key=True)
	flag=models.ImageField(blank=True, null=True)
	shortname = models.CharField(max_length=256, unique=True)
	#description=models.TextField(max_length=500,blank=True, null=True)
	description=models.TextField(max_length=555,default="about your country")
class PlayerGroup(abst):
	#name=models.CharField(max_length=250)
	country = models.ForeignKey(Country,on_delete=models.PROTECT)
	players = models.ManyToManyField(Player)

	def __str__(self):
		return self.name

class Match(abst):
	#name=models.CharField(max_length=250)
	country=models.ForeignKey(Country, on_delete=models.PROTECT)
	stadium = models.CharField(max_length=250)
	group1 = models.ForeignKey(PlayerGroup,on_delete=models.PROTECT,
		related_name="group1")
	group2 = models.ForeignKey(PlayerGroup,on_delete=models.PROTECT,
		related_name="group2")

