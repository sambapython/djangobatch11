from django import forms
from info.models import Player, UserProfile, Match,Country, PlayerGroup
'''
class MatchSearchForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		kwargs["use_required_attribute"]=False
		kwargs["empty_permitted"]=True
		forms.ModelForm.__init__(self,*args,**kwargs)
	class Meta:
		model = Match
		fields = "__all__"
'''
class MatchSearchForm(forms.Form):
	countries = [(i.id,i.name) for i in Country.objects.all()]
	groups = [(i.id,i.name) for i in PlayerGroup.objects.all()]
	stadiums =[(j,j) for j in set([i.stadium for i in Match.objects.all()])]
	countries.insert(0,("",""))
	groups.insert(0,("",""))
	stadiums.insert(0,("",""))

	name=forms.CharField(max_length=250,required=False)
	country= forms.ChoiceField(choices=countries, required=False)
	stadium = forms.ChoiceField(choices=stadiums,required=False)
	group1 = forms.ChoiceField(choices=groups,required=False)
	group2 = forms.ChoiceField(choices=groups,required=False)
	page=forms.IntegerField(required=False)
	


class RegistrationForm(forms.ModelForm):
	confirm_password = forms.CharField(max_length=250)
	class Meta:
		model = UserProfile
		fields = ["username","password","country"]
	def clean_password(self):
		password = self.data.get("password")
		c_password=self.data.get("confirm_password")
		if password!=c_password:
			err = "passwords not matched"
			raise forms.ValidationError(err)
		return password
class LoginForm(forms.Form):
	username = forms.CharField(max_length=250)
	password = forms.CharField(widget=forms.PasswordInput)
	
class PlayerForm(forms.ModelForm):
	#name=forms.CharField(source="name", validators)
	class Meta:
		model = Player
		fields = "__all__" #["name","dob"]
		

	def clean_name(self,value=None):
		name=self.data.get("name")
		if not name.isalnum():
			raise forms.ValidationError("name not allowed special symbols..")
		return name

