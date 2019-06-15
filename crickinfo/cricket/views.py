from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def matches_view(request):
	return render(request, "cricket/matches.html")
def fun(request):
	# read the data from cricket/teplates/players.html and create HttpResponse
	resp = render(request, "cricket/players.html")
	return resp
def add_view(request):
	data = request.GET
	if data:
		a=float(data["a"])
		b=float(data["b"])
		c=a+b
	else:
		c=0
		a=0
		b=0
	return render(request, "cricket/add.html",
		{"res":c,"a":a,"b":b})
