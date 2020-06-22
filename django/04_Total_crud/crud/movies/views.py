from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Movie, Comment
from .forms import MovieForm, CommentForm

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


# def new(request):
#     return render(request, 'movies/new.html')


# def create(request):
#     title = request.POST.get('title')
#     title_en = request.POST.get('title_en')
#     audience = request.POST.get('audience')
#     open_date = request.POST.get('open_date')
#     genre = request.POST.get('genre')
#     watch_grde = request.POST.get('watch_grade')
#     score = request.POST.get('score')
#     poster_url = request.POST.get('poster_url')
#     description = request.POST.get('description')

#     movies = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, 
#                     watch_grade=watch_grde, score=score, poster_url=poster_url, description=description)
#     movies.save()

#     return render(request, 'movies/index.html')

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else: # POST  가 아닌 다른 메서드일때만 동작
        form = MovieForm()
    context = {
        # 1. POST가 아닐 때(else) form = 빈 form 보여주기
        # 2. is)valid 에서 걸려서 내려온 form = 에러 메세지가 포함된 form 을 보여줌
        'form': form,
    }
    return render(request, 'movies/create.html', context)



def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comments = movie.comment_set.all()
    form = CommentForm()
    context = {
        'movie': movie,
        'comments': comments,
        'form': form,
    }
    return render(request, 'movies/detail.html', context)


# def edit(request, pk):
#     movies = Movie.objects.get(pk=pk)
#     context = {
#         'movies': movies,
#     }
#     return render(request, 'movies/edit.html', context)


# def update(request, pk):
#     movies = Movie.objects.get(pk=pk)

#     movies.title = request.POST.get('title')
#     movies.title_en = request.POST.get('title_en')
#     movies.audience = request.POST.get('audience')
#     movies.open_date = request.POST.get('open_date')
#     movies.genre = request.POST.get('genre')
#     movies.watch_grde = request.POST.get('watch_grade')
#     movies.score = request.POST.get('score')
#     movies.poster_url = request.POST.get('poster_url')
#     movies.description = request.POST.get('description')
#     movies.save()

#     return redirect('movies:detail', movies.pk)


@require_http_methods(["GET", "POST"])
def edit(request, pk):
    movies = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movies)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movies.pk)
    else:
        form = MovieForm(instance=movies)
    context = {
        'form': form,
    }
    return render(request, 'movies/edit.html', context)
    


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)
    


# def create(request):
#     if request.method == 'POST':
#         form = MovieForm(request.POST)
#         if form.is_valid():
#             movie = form.save()
#             return redirect('movies:detail', movie.pk)
#     else: # POST  가 아닌 다른 메서드일때만 동작
#         form = MovieForm()
#     context = {
#         # 1. POST가 아닐 때(else) form = 빈 form 보여주기
#         # 2. is)valid 에서 걸려서 내려온 form = 에러 메세지가 포함된 form 을 보여줌
#         'form': form,
#     }
#     return render(request, 'movies/create.html', context)


@require_POST
def comment_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    # content = request.POST.get('content')
    # Comment.objects.create(movie=movie, content=content)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.movie = movie
        comment.save()

    return redirect('movies:detail', movie.pk)

@require_POST
def comment_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    
    comment.delete()
    
    return redirect('movies:detail', movie_pk)

