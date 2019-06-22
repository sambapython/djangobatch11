"""cricketinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from info.views import home_view, players_view, countries_view,\
create_country_view, update_country_view,delete_country_view,\
create_player_view, update_player_view,delete_player_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view),
    path("players/", players_view),
    path("countries/", countries_view),
    path("create_country/",create_country_view),
    re_path("update_country/(?P<pk>[0-9]+)",update_country_view),# update_country_view(reobj,pk=23)
    re_path("delete_country/(?P<pk>[0-9]+)",delete_country_view), 
    path("create_player/",create_player_view),
    re_path("update_player/(?P<pk>[0-9]+)",update_player_view),# update_country_view(reobj,pk=23)
    re_path("delete_player/(?P<pk>[0-9]+)",delete_player_view), 
]
