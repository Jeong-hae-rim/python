from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import PostForm
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)


@login_required
def like(request, post_pk):
    user = request.user
    post = get_object_or_404(Post, pk=post_pk)

    # user.like_posts = > user가 좋아요 버튼을 누른 게시물들
    # post.like_users => post에 좋아요 버튼을 누른 유저들

    if post in user.like_posts.all():
        #이미 누른 경우
        user.like_posts.remove(post)
        liked = False
    else:
        #아직 안 누른 경우
        user.like_posts.add(post)
        liked = True
    #return redirect('posts:index')
    print("like 함수")
    likedalls = post.like_users.all()
    li = []
    for likedall in likedalls:
        li.append(likedall.username)
    print(li)
    context = {
        'msg': '게시글을 좋아합니다.',
        'liked': liked,
        'li':li,
      
    }

    return JsonResponse(context)

