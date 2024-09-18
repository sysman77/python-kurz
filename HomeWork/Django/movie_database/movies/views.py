from django.shortcuts import render
from .models import Film

def homepage(request):
    return render(request, 'movies/homepage.html')

def film_list(request):
    filmy = Film.objects.all()
    return render(request, 'movies/film_list.html', {'filmy': filmy})

def film_detail(request, film_id):
    film = Film.objects.get(id=film_id)
    return render(request, 'movies/film_detail.html', {'film': film})