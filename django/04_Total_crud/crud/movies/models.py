from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=50)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=50)
    watch_grade = models.CharField(max_length=50)
    score = models.FloatField()
    poster_url = models.CharField(max_length=200)
    description = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    # N -> 1 : comment.movie
    # 1 -> N(역참조) : movie.comment_set