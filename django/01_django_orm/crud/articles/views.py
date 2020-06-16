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


    return redirect('articles:index')
    #return render(request, 'articles/index.html')