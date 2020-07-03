from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404
from django.forms.models import model_to_dict
from django.core import serializers
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import datetime
import json, os, urllib.request, mimetypes, time, dateutil.parser
from pprint import pprint
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from .models import Api
from statuses.models import Status
from datetime import timedelta
import pytz

# Create your views here.
def index(request):
    apis = Api.objects.all()
    total_apis = apis.count()
    #good_apis
    bad_apis = 0
    for api in apis:
        latest_status = Status.objects.filter(api_id=api.id).latest('updated_time')
        print(latest_status.status)
        if latest_status.status != 'INFO-000':
            bad_apis += 1
   
    context = {
        'apis' : apis,
        'total_apis' : total_apis,
        'good_apis' : total_apis - bad_apis,
        'bad_apis' : bad_apis,
    }
    return render(request, 'apis/index.html', context)

def about(request):
    return render(request, 'apis/about.html')

def detail(request, pk):
    # 추후 누적값을 저장할 코드 구현 --> Status app (DB 저장)
    api = get_object_or_404(Api,pk=pk)
    # print(api.download_users)
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
    user = request.user
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
    result = []
    local_timezone = pytz.timezone('Asia/Seoul')

    statuses = Status.objects.filter(api_id=pk, updated_time__range=[datetime.now()-timedelta(days=3), datetime.now()])

    for status in statuses:
        if status.status == 'INFO-000':
            value_val = 1
            status_val = '정상'
        else:
            value_val = 0
            status_val = '다운'
            
        # 타임존 변경해야 그래프에 정상 출력
        date = status.updated_time.strftime("%Y-%m-%d %H:%M:%S")
        date_str = dateutil.parser.parse(date)
        local_date = date_str.replace(tzinfo=pytz.utc).astimezone(local_timezone)

        status_obj = {
            'date': local_date,
            'value': value_val,
            'status': status_val,
        }
        result.append(status_obj)

    context = {
        "msg" : "success",
        "result" : result
    }
    return JsonResponse(context)
