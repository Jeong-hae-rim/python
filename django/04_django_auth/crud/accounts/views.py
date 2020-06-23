from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# form .forms import ArticleForm 과 같음.
from django.contrib.auth import login as auth_login
# 로그인 가져오기
from django.contrib.auth import logout as auth_logout
# 로그아웃 가져오기

# Create your views here.

def signup(request):
    # user가 가입 했을 때, create를 하는 역할
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

# 구글에서 django github
# python manage.py migrate 해보면 auth.으로 되있는 메세지가 뜸..
# class User는 (AbstaractUser)를 상속받음, 얘는 AbstaractBaseUser상속 받고, 얘는 models.model을 상속받음..
# django usercreationform 검색 2번째 사이트 - 컨트롤 f 유저크리에이션폼 검색
# django.contrib.auth.forms


# 위에 장고에서 불러온게 장고 로그인 따라서 함수 이름 겹침
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # request, data 필수인자
        if form.is_valid():
            # form.save()가 아닌 이유.
            # 로그인은 인증만 하는 과정이므로...
            # 검증만한다.
            auth_login(request, form.get_user()) # 2번째 인자로 실제 유저 정보.
            # 장고에서 제공하는 로그인
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context) # request에 user 정보가 들어가 있음.
    
# 로그인은 사용자 정보를 바탕으로 디비랑 비교하고 세션을 생성하는것
# 로그아웃은 세션을 파기하는 것.


def logout(request):
    auth_logout(request) # request에는 user정보가 담겨있음.
    return redirect('accounts:login')