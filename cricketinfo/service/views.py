from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from info.models import Country, Player
from service.serializers import CountrySerializer, PlayerSerializer,\
PlayerPutSerializer
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.core.cache import cache
from django.conf import settings
class TokenView(APIView):
	authentication_classes=[]
	permission_classes=[]
	def post(self, request):
		params = request.data
		user = authenticate(username=params["username"],
			password=params["password"])
		if user:
			t=Token(user=user)
			try:
				t.save()
			except:
				t = Token.objects.get(user=user)
			return Response(t.key)
		else:
			return Response("Not authenticated",
				status=status.HTTP_401_UNAUTHORIZED)
class PlayerView(viewsets.ModelViewSet):
	# create, update, destroy, list, retrieve
	serializer_class=PlayerSerializer
	queryset=Player.objects.all()
	def retrieve(self,request,pk, **kwargs):
		resp = cache.get("player_%s"%pk)
		if resp:
			return resp
		else:
			resp = viewsets.ModelViewSet.retrieve(self,request,pk,**kwargs)
			return resp
	def get_serializer_class(self):
		if self.action == "update":
			return PlayerPutSerializer
		else:
			return self.serializer_class

	def destroy(self,request,pk,**kwargs):
		resp = viewsets.ModelViewSet.destroy(self,request,pk,**kwargs)
		if resp.status_code==204:
			cache.delete("player_%s"%pk)
		return Response("Id: %s deleted successfully!!" % pk)



# Create your views here.
resp = {"message":"","details":""}
class CountryView(APIView):
	def get(self,request,pk=None,format=None):
		if pk:
			data = cache.get("country_%s"%pk)
			if not data:
				data =Country.objects.filter(id=pk)
				cache.set("country_%s"%pk,data)
		else:
		    data = Country.objects.all()
		ser = CountrySerializer(data, many=True)
		#countries = [c.name for c in data]
		return Response(ser.data)
	def post(self,request, format=None):
		data = request.data
		ser = CountrySerializer(data=data)
		if ser.is_valid():
			c=Country(**ser.data)
			for db in settings.DATABASES:
				c.save(using=db)
			resp["message"] = "Country created successfully"
			resp["details"] = ser.data
			return Response(resp)
		else:
			resp["message"]="Country creatioin failed"
			resp["details"] = ser._errors
			return Response(resp, status=status.HTTP_400_BAD_REQUEST)
	def put(self,request,pk,format=None):
		inst = Country.objects.get(id=pk)
		ser = CountrySerializer(instance=inst,data=request.data, partial=True)
		if ser.is_valid():
			ser.save()
			resp["message"] = "Country updated successfully"
			resp["details"] = ser.data
			cache.delete("country_%s"%pk)
			return Response(resp)
		else:
			resp["message"]="Country updation failed"
			resp["details"] = ser._errors
			return Response(resp, status=status.HTTP_400_BAD_REQUEST)
	def delete(self,request,pk,format=None):
		inst = Country.objects.filter(id=pk) #[rec1]
		if inst:
			inst=inst[0]
			try:
				inst.delete()
			except Exception as err:
				resp["message"] = "some error"
				resp["details"] = str(err) 
				return Response(resp,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
			resp["message"] = "deletion success"
			resp["details"] = "%s"%pk
			cache.delete("country_%s"%pk)
			return Response(resp)
		else:
			resp["message"] = "deletion failed"
			resp["details"] = "Record not found" 
			return Response(resp,status=status.HTTP_404_NOT_FOUND)