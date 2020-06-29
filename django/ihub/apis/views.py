from django.shortcuts import render
from .models import Api
# Create your views here.


def apis(request):
    apis = Api.objects.all()
    context = {
        'apis' : apis
    }
    return render(request, 'apis/apis.html', context)


def index(request):
    return render(request, 'apis/index.html')