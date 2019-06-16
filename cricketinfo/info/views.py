from django.shortcuts import render
from info.models import Country

# Create your views here.
def players_view(request):
	return render(request,"info/players.html")
def home_view(request):
	return render(request,"info/home.html")
def countries_view(request):
	return render(request,"info/countries.html")
def create_country_view(request):
	msg=""
	if request.method=="POST":
		data=request.POST
		cnt = Country(name=data["name"],
			shortname=data["shortname"],
			description=data["description"]
			)
		try:
			cnt.save()
			msg="Country created successfully"
		except Exception as err:
			msg=err
		
	return render(request,"info/create_country.html",{"message":msg})