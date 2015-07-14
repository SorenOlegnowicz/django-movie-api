from django.core.urlresolvers import reverse
from rest_framework import generics, serializers
from movie.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    earl = serializers.SerializerMethodField()

    def get_earl(self, obj):
        return reverse('all_things', kwargs={"pk": obj.pk})
        
    class Meta:
        model = Movie
        fields = ['earl', 'title']


class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieAllThingsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer