from django.contrib import admin
from .models import Articles


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'content', 'created_at']

admin.site.register(Articles, ArticleAdmin)