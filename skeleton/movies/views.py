from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_safe
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer
from rest_framework.response import Response

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    serializer = MovieSerializer(movie)
    data = serializer.data
    context = {
        
    }
    check = data['genres']
    data['names'] = []
    for i in check:
        genre = Genre.objects.get(id = i)
        serializer_g = GenreSerializer(genre)
        serializer_g.data['name']
        data['names'].append(serializer_g.data['name'])
    del(data['genres'])
    context['data'] = data
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    movies = Movie.objects.all()
    vote_order = movies.order_by('-vote_average')[:10]
    popularity_order = movies.order_by('-popularity')[:10]
    choice = []
    for i, j in zip(vote_order, popularity_order):
        choice.append((i, j))
    context = {
        'choices' : choice,
    }
    return render(request, 'movies/recommended.html', context)