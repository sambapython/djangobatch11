from django.shortcuts import render

# Create your views here.
def home_view(request):
	return render(request,"operations/home.html")
def add_view(request):
	data = request.GET
	if data:
		a=float(data["a"])
		b=float(data["b"])
		c=a+b
	else:
		a=0
		b=0
		c=0
	return render(request,"operations/add.html",{"a":a,"b":b,"c":c})
