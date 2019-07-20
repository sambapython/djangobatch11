from django.http import HttpResponse
from django.shortcuts import render, redirect
class Tracker:
    def __init__(self, view):
        self.view = view

    def __call__(self,request):
        print("write a code to do something before request")
        resp = self.view(request)
        print("do someting after gettign a response")
        if resp.status_code==404:
            return render(request,"info/404.html")
        return resp
        #return HttpResponse("we are in maintananance mode")
