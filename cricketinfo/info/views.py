from django.shortcuts import render, redirect
from info.models import Country, Player
from info.forms import PlayerForm, RegistrationForm, LoginForm
def players_view(request):
	players = Player.objects.all()
	return render(request,"info/players.html",
		{"players":players})
def delete_player_view(request, pk):
	pass
def update_player_view(request,pk):
	player = Player.objects.filter(id=pk)
	msg=""
	if player:
		player = player[0]
		form = PlayerForm(instance=player)
		if request.method=="POST":
			new_data = request.POST
			form = PlayerForm(instance=player,data=new_data)
			if form.is_valid():
				form.save()
				return redirect("/players")
			else:
				msg=form._errors
	else:
		msg="player not found"
	return render(request,"info/update_player.html",{"form":form,"message":msg})
	
def create_player_view(request):
	msg=""
	if request.method=="POST":
		data = request.POST
		form = PlayerForm(data=data)
		if form.is_valid():
			form.save()
			return redirect("/players")
		else:
			msg = form._errors

	else:
		form = PlayerForm()
		
	return render(request,"info/create_player.html",{"form":form,"message":msg})


def countries_view(request):
	countries = Country.objects.all()
	return render(request,"info/countries.html",
		{"countries":countries})

def delete_country_view(request, pk):
	country = Country.objects.filter(id=pk)
	if country:
		country=country[0]
		msg=""
		if request.method=="POST":
			country.delete()
			msg="country deleted successfully"
			return redirect("/countries")
	else:
		msg="country not found"
		
	return render(request, "info/delete_country.html",
		{"data": country,"message":msg})
def update_country_view(request,pk):
	country = Country.objects.filter(id=pk)
	if country:
		country=country[0]
		msg=""
		if request.method=="POST":
			data = request.POST
			country.name=data["name"]
			country.description=data["description"]
			country.shortname=data["shortname"]
			country.save()
			msg="country updated successfully"
			return redirect("/coutries")
	else:
		msg="country not found"
	return render(request, "info/update_country.html",
		{"data": country,"message":msg})
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
			return redirect("/countries")
		except Exception as err:
			msg=err
		
	return render(request,"info/create_country.html",{"message":msg})


def home_view(request):
	reg_form = RegistrationForm()
	login_form = LoginForm()
	return render(request,"info/home.html",{"reg_form":reg_form,
		"login_form":login_form})
