# Create your views here.
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from movie.models import Movie


class MovieListView(ListView):
    model = Movie


class MovieCreateView(CreateView):
    model = Movie
    fields = ['title']
    success_url = '/movie_list'


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = '/movie_list'


class MovieDetailView(DetailView):
    model = Movie


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ["title"]
    template_name = 'movie/update_movie.html'
    success_url = reverse_lazy('movie_list')

def home_view(request):
    context = {}
    return render_to_response('base.html', context)
