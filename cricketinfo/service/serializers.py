from rest_framework import serializers
from info.models import Country, Player
class PlayerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Player
		exclude = ["pic"]
class PlayerPutSerializer(serializers.ModelSerializer):
	def __init__(self,*args,**kwargs):
		kwargs["partial"]=True
		serializers.ModelSerializer.__init__(self,*args, **kwargs)
	class Meta:
		model = Player
		exclude = ["pic"]
class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ["id","name","shortname","description"]
	def validate_name(self, value):
		if " " in value:
			raise serializers.ValidationError("Not allowing space in the name")
		return value