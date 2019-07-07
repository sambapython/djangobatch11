from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from info.models import Country, Player
from service.serializers import CountrySerializer, PlayerSerializer
from rest_framework import status
from rest_framework import viewsets
class PlayerView(viewsets.ModelViewSet):
	serializer_class=PlayerSerializer
	queryset=Player.objects.all()

# Create your views here.
resp = {"message":"","details":""}
class CountryView(APIView):
	def get(self,request,pk=None,format=None):
		if pk:
			data =Country.objects.filter(id=pk)
		else:
		    data = Country.objects.all()
		ser = CountrySerializer(data, many=True)
		#countries = [c.name for c in data]
		return Response(ser.data)
	def post(self,request, format=None):
		data = request.data
		ser = CountrySerializer(data=data)
		if ser.is_valid():
			ser.save()
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
			return Response(resp)
		else:
			resp["message"] = "deletion failed"
			resp["details"] = "Record not found" 
			return Response(resp,status=status.HTTP_404_NOT_FOUND)