from django.shortcuts import render, redirect
from .models import Page

# Create your views here.

def index(request):
    pages = Page.objects.all()

    context = {
        'pages': pages,
    }

    return render(request, 'pages/index.html', context)


def new(request):
    return render(request, 'pages/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    pages = Page(title=title, content=content)
    pages.save()

    return redirect('pages:index')


def detail(request, pk):
    pages = Page.objects.get(pk=pk)
    context = {
        'pages':pages,
    }
    return render(request, 'pages/detail.html', context)


def delete(request, pk):
    pages = Page.objects.get(pk=pk)
    pages.delete()
    return redirect('pages:index')


def edit(request, pk):
    pages = Page.objects.get(pk=pk)
    context = {
        'pages': pages,
    }
    return render(request, 'pages/edit.html', context)


def update(request, pk):
    pages = Page.objects.get(pk=pk)

    pages.title = request.POST.get('title')
    pages.content = request.POST.get('content')
    pages.save()

    return redirect('pages:detail', pages.pk)