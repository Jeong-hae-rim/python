# django import style guide
# 1. standard library
# 2. 3rd party library
# 3. django
# 4. local django
 
import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    foods = ['족발', '샐러드', '치킨', '연어덮밥']
    pick = random.choice(foods)
    context = {
        'pick': pick,
    }
    return render(request, 'dinner.html', context)


def randomimg(request):
    URL = 'https://picsum.photos/200/300.jpg'
    context = {
        'URL': URL,
    }
    return render(request, 'randomimg.html', context)


def hello(request, name):
    context = {
        'name': name
    }
    return render(request, 'hello.html', context)


def introduce(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'introduce.html', context)


def multiplication(request, front, back):
    result = front * back
    context = {
        'result': result,
    }
    return render(request, 'multiplication.html', context)

def dtl_practice(request):
    foods = ['짜장면', '초밥', '차돌짬뽕', '콩국수']
    empty_list = []
    messages = 'Life is short, You need Python'
    context= {
        'foods': foods,
        'empty_list': empty_list,
        'messages': messages,
    }
    return render(request, 'dtl_practice.html', context)