from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
	# read the data from cricket/teplates/players.html and create HttpResponse
	resp = render(request, "cricket1/players.html")
	return resp
