# Create your views here.
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from movie.models import Movie

@csrf_exempt
def movie_list(request):
    if request.method == 'GET':
        qs = Movie.objects.all()
        return HttpResponse(serializers.serialize("json", qs), content_type="application/json")
    elif request.method == 'POST':
        print("Run")
        data = request.POST
        print(data)
        movie = Movie.objects.create(title=data["title"])
        return HttpResponse(serializers.serialize("json", [movie]), status=201, content_type="application/json")

def movie_detail(request, model_pk):
    if request.method == "GET":
        detail = Movie.objects.filter(id=model_pk)
        if detail:
            return HttpResponse(serializers.serialize("json", detail), content_type="application/json")
        return HttpResponse([], status=404)
   # elif request.method == "PATCH":
   #     print(request.POST)
   # How do this Joel?
