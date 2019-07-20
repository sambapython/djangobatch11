from django.conf import settings
from django.http import HttpResponse
import requests
from info.models import UserProfile, Country
from django.shortcuts import redirect
from django.contrib.auth import login
def googleauth_view(request):
    token_request_uri = "https://accounts.google.com/o/oauth2/auth"
    response_type = "code"
    client_id = settings.CLIENT_ID
    redirect_uri = "http://localhost:8000/redirect_auth/"
    scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
    url = f"{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
    resp = requests.get(url)
    return HttpResponse(resp.text)

def redirect_auth_view(request):
    code=request.GET.get('code')
    access_token_uri = 'https://accounts.google.com/o/oauth2/token'
    redirect_uri = "http://localhost:8000/redirect_auth/"
    resp = requests.post(access_token_uri, json={
        'code':code,
        'redirect_uri':redirect_uri,
        'client_id':settings.CLIENT_ID,
        'client_secret':settings.CLIENT_SEC,
        'grant_type':'authorization_code'
    })
    token_data = resp.json().get("access_token")
    resp = requests.get(f"https://www.googleapis.com/oauth2/v1/userinfo?access_token={token_data}")
    user_data = resp.json()
    username = user_data.get("email")
    user = UserProfile.objects.filter(username=username)
    if not user:
        c=Country.objects.all()
        user = UserProfile.objects.create_user(username=username,
            password="123456778",country=c[0])
    else:
        user=user[0]
    request.session.update({"picture":user_data.get("picture")})
    login(request,user)
    return redirect("/")
