from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def new(request):
    return render(request, 'movies/new.html')


def detail(request, pk):
    movies = Movie.objects.get(pk=pk)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/detail.html', context)


def create(request):
    title = request.POST.get('title')
    title_en = request.POST.get('title_en')
    audience = request.POST.get('audience')
    open_date = request.POST.get('open_date')
    genre = request.POST.get('genre')
    watch_grde = request.POST.get('watch_grade')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    movies = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, 
                    watch_grade=watch_grde, score=score, poster_url=poster_url, description=description)
    movies.save()

    return render(request, 'movies/index.html')


def edit(request, pk):
    movies = Movie.objects.get(pk=pk)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/edit.html', context)


def update(request, pk):
    movies = Movie.objects.get(pk=pk)

    movies.title = request.POST.get('title')
    movies.title_en = request.POST.get('title_en')
    movies.audience = request.POST.get('audience')
    movies.open_date = request.POST.get('open_date')
    movies.genre = request.POST.get('genre')
    movies.watch_grde = request.POST.get('watch_grade')
    movies.score = request.POST.get('score')
    movies.poster_url = request.POST.get('poster_url')
    movies.description = request.POST.get('description')
    movies.save()

    return redirect('movies:detail', movies.pk)




def delete(request, pk):
    movies = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        movies.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movies.pk)
    

