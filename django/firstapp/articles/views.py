# django import style guide
# 1. standard library - 내가 직접 설치하지 않은 라이브러리
# 2. 3rd party library - 외부에서 설치한 라이브러리
# 3. django
# 4. local django

import random
import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    foods = ['족발', '샐러드', '치킨', '연어 덮밥']
    pick = random.choice(foods)
    context = {
        'pick': pick,
    }
    return render(request, 'dinner.html', context)
    # 'pick' > dinner.html에서 사용할 키 이름.
    # 오른쪽 pick 뿌릴 데이터 값


def randomimg(request):
    URL = 'https://picsum.photos/200/300.jpg'
    context = {
        'URL': URL,
    }
    return render(request, 'randomimg.html', context)


def hello(request, name):
    context = {
        'name': name,

    }
    return render(request, 'hello.html', context)


def introduce(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'introduce.html', context)


def multiplication(request, front, back):
    result = front*back
    context = {
        'result': result,
    
    }
    return render(request, 'multiplication.html', context)