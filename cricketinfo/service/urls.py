from service.views import CountryView, PlayerView,TokenView
from django.urls import path,re_path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("player",PlayerView)
#router.register("country/",CountryView)
#urlpatterns = router.urls

urlpatterns = [
	path("",include(router.urls)),
	path("token/",TokenView.as_view()),
    path("country/", CountryView.as_view()),
    re_path("country/(?P<pk>[0-9]+)/",CountryView.as_view())
]