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
