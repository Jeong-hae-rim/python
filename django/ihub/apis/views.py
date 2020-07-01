from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404
from django.forms.models import model_to_dict
from django.core import serializers
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import datetime
import json, os, urllib.request, mimetypes, time
from pprint import pprint
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from .models import Api
from statuses.models import Status


# Create your views here.
def index(request):
    apis = Api.objects.all()
    context = {
        'apis' : apis
    }
    return render(request, 'apis/index.html', context)

def detail(request, pk):
    # 추후 누적값을 저장할 코드 구현 --> Status app (DB 저장)
    api = get_object_or_404(Api,pk=pk)
    #print(api.download_users)
    context = {
        'msg' : 'success',
        'api_name' : api.api_name,
        'api_url' : api.api_url,
        'latest_modified_date' : api.latest_modified_date,
        'copyright' : api.copyright,
        'copyright_range' : api.copyright_range,
        'api_file' : api.api_file,
        'download_users' : api.download_users.all().count()
    }

    return JsonResponse(context)

def search(request, search_string):
    api = get_object_or_404(Api, api_name=search_string)
    context = {
        'msg' : 'success',
        'api_pk' : api.pk
    }
    return JsonResponse(context) 

def status(request, pk):
    #status = get_object_or_404(Status, api_id=pk)
    latest_status = Status.objects.filter(api_id=pk).latest('updated_time')
    print(latest_status.updated_time)
    context = {
        'msg' : 'success',
        'latest_status' : latest_status.status
    }
    return JsonResponse(context) 

def download(request, pk):
    api = get_object_or_404(Api, pk=pk)
    file_path = os.path.join(settings.MEDIA_ROOT, api.api_file)
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_path)[0])
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def graph(request, pk):
    #statues = get_object_or_404(Status, pk=pk)
    #var data =  [{
    #    "date": new Date(2020, 07, 01, 10, 1),
    #    "value":1,
    #    "status":"정상"
    #}];

    statues = Status.objects.filter(api_id=pk)
    # var data =  [{
    #     "date": "datetime.datetime",
    #     "value":1,
    #     "status":"정상"
    # }]
    context = {
        "msg" : "success"
    }
    return JsonResponse(context)
    
def ranking(request):
    url = 'http://data.seoul.go.kr/'
    print('------------------------')
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=options)
    driver.get(url)
    time.sleep(1)
    api_list = driver.find_elements_by_xpath(
        '//*[@id="tabPopData1"]/ul/li/a')
    result = []
    api_rank = 1
    for api in api_list:
        # print(dir(api))
        api_name = api.find_element_by_class_name('bbs-txt').text
        pprint(api_name)
        api_url = api.get_attribute('href')
        api_obj = {
            'api_name': api_name,
            'api_url': api_url,
            'api_rank': api_rank,
        }
        result.append(api_obj)
        api_rank += 1
    print(result[0].get('api_name'))
    context = {
        'msg' : 'success',
        'result': result,
    }
    return JsonResponse(context)

