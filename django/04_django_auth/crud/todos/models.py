from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=100)
    due_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 내가 연결하고 싶은 모델 이름, on_delete =
    # settings.AUTH_USER_MODEL : 장고가 들고 있는 유저 모델을 가져오란 뜻
    
