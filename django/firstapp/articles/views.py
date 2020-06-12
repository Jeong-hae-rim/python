# django import style guide
# 1. standard library
# 2. 3rd party library
# 3. django
# 4. local django
 
import random
from pprint import pprint 
from datetime import datetime
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
    datetime_now = datetime.now()
    context= {
        'foods': foods,
        'empty_list': empty_list,
        'messages': messages,
        'datetime_now': datetime_now,
    }
    return render(request, 'dtl_practice.html', context)


def palin(request, word):
    if word == word[::-1]:
        result = True
    #word2 = word[::-1]
    else:
        result = False
    context = {
        'word': word,
        'result': result
        #'word': word,
        #'word2': word2,
    }
    return render(request, 'palin.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):

    message = request.GET.get('message')
    letter = request.GET.get('letter')

    context={
        'message': message,
        'letter' : letter,
    }

    #pprint(request.META)
    #print(request.GET.get('message'))
    #.get은 쿼리를 받아올 때 없는 쿼리라면 none을 발생.
    # 서버 기동시 서버를 아예 다운시키는 것보단 저게 더 효율적
    return render(request, 'catch.html', context)