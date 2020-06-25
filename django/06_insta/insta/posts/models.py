from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=200)
    #작성한 사람을 저장
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    #image = models.ImageField()
    image = ProcessedImageField(upload_to='media',
                                processors=[ResizeToFill(500, 500)],
                                format='JPEG',
                                options={'quality': 60})
    #좋아요 버튼을 누른 사람들 저장
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    class Meta:
        ordering = ['-id']

'''
class user
    # post_set = FK -> 어떤 유저가 작성한 글들 
    # like_posts(이전에는 post_set) = M2M -> 어떤 유저가 조항요 버튼 누른 글들
    ==> related_name='like_posts'로 설정을 해줌으로써
    ===> post_set 에서 like_posts로 변수 명이 덮어 씌워짐
'''