from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})


def home(request):
    return render(request, 'movie/home.html')


def about(request):
    return render(request, 'movie/about.html')
