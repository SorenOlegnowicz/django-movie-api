from django.conf.urls import url
from api_framework import views



urlpatterns = [
    url(r'movie/$', views.MovieListAPIView.as_view()),
    url(r'^movie/(?P<pk>\d+)/detail/$', views.MovieDetailAPIView.as_view()),
    url(r'^movie/(?P<pk>\d+)/$', views.MovieAllThingsAPIView.as_view(), name='all_things'),
]