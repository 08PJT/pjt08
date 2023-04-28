from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.decorators.http import require_safe, require_POST
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer
from rest_framework.response import Response
from django.http import JsonResponse

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
    selected_genre = request.GET.get('genre')
    print(selected_genre)
    movies_list = Movie.objects.all().order_by('-vote_average')[:10]
    # if selected_genre:
    #     movies_list = movies_list.filter(genres__name=selected_genre)
    
    genres = Genre.objects.all()
    context = {
        'movies_list': movies_list,
        'genres': genres,
    }
    return render(request, 'movies/recommended.html', context)

@require_POST
def like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
            like_movie = False
        else:
            movie.like_users.add(user)
            like_movie = True
        context = {
            'like_movie': like_movie,
            'likes_count' : movie.like_users.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:login')