from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all() #ORM 문법이라 경고가 계속 뜨는 것임
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    #요청을 보내기만 하기 때문에 다른 처리할 게 없음
    return render(request, 'articles/new.html')


def create(request):
    #데이터랑 실제 왔다갔다 하는 부분
    #1. new에서 보낸 데이터 받기
    title = request.POST.get('title') #request.GET.get('title')
    content = request.POST.get('content') #request.GET.get('content')

    #2. DB에 저장
    '''
    article = Article()
    article.title = title
    article.content = content
    article.save()
    -> 컬럼 많아지면 귀찮아짐

    Article.objects.create(title=title, content=content)
    -> 데이터 유효성 검사를 할 타이밍이 나오지 않음
    '''

    article = Article(title=title, content=content)
    #데이터가 유효한지 검사.
    article.save()


    return redirect('articles:detail', article.pk)
    #return render(request, 'articles/index.html')


def detail(request, pk):
    article = Article.objects.get(pk=pk) #오른쪽 pk는 variable routing의 pk
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    #print(request.method)
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def edit(request, pk):
    #요청을 보내기만 하기 때문에 다른 처리할 게 없음
    #다만 어떤 글인지는 알아야 하기 때문에
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    #1. edit에서 보낸 데이터를 받아야 한다.

    '''
    title = request.POST.get('title') 
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    >> 너무 코드가 반복되는 느낌이니 합쳐보자!
    '''

    article.title = request.POST.get('title') 
    article.content = request.POST.get('content')
    article.save() 

    return redirect('articles:detail', article.pk)