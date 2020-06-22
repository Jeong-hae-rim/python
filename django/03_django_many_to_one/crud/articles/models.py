from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comment_set = (자동으로 만들어주는 것)

    

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    #article_id = (완전히 FK로서 동작함. 보이지 않지만 만들어줌. 장고 내부에서 가지고 있는 기능.)
    #Article에 속해있음

