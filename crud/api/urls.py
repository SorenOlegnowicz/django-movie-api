from django.conf.urls import include, url
from django.contrib import admin

from api.views import movie_list, movie_detail


urlpatterns = [
    url(r'^moovy/$', movie_list),
    url(r'^moovy/(?P<model_pk>\d+)/$', movie_detail),
]