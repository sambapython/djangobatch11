from django.db import models

# Create your models here.
from rest_framework.authtoken.models import Token
class MyToken(Token):
	expire_time = models.IntegerField(blank=True, null=True)