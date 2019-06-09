from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def matches_view(request):
	return render(request, "cricket/matches.html")
def fun(request):
	# read the data from cricket/teplates/players.html and create HttpResponse
	resp = render(request, "cricket/players.html")
	return resp
