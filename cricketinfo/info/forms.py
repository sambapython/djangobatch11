from django import forms
from info.models import Player, UserProfile

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

