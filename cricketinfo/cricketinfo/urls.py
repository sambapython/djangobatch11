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
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, re_path, include
from info.views import home_view, players_view, countries_view,\
create_country_view, update_country_view,delete_country_view,\
create_player_view, update_player_view,delete_player_view, logout_view,\
MatchListView
from info.google import googleauth_view, redirect_auth_view
from django.views.generic import ListView, CreateView, DeleteView,\
UpdateView
from info.models import Match,PlayerGroup
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("redirect_auth/",redirect_auth_view),
    path("googleauth/",googleauth_view),
    path("api/", include("service.urls")),
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
    path("matches/",login_required(MatchListView.as_view(
        model=Match,
        queryset = Match.objects.all(),
        #template_name= "info/match_list.html"
        ))),
    path("create_match", login_required(CreateView.as_view(
            model=Match,
            fields = "__all__",
            #template_name="info/match_form.html"
            success_url="/matches"
        ))),
    path("create_group/",login_required(CreateView.as_view(
        model = PlayerGroup,
        fields="__all__",
        success_url="/matches"
        #template_name="info/playergroup_form.html"
        ))),
    re_path("delete_match/(?P<pk>[0-9]+)",login_required(DeleteView.as_view(
        model=Match,
        success_url="/matches",
        template_name="info/match_delete.html"
        ))),
    re_path("update_match/(?P<pk>[0-9]+)",login_required(UpdateView.as_view(
        model=Match,
        success_url="/matches",
        fields="__all__",
        #template_name="info/match_form.html"
        ))),
    path("logout/",logout_view),
]
urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

