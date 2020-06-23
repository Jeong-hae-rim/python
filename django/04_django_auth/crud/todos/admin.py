from django.contrib import admin
from .models import Todo 

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'content', 'due_date',]
    list_editable = ['content']

admin.site.register(Todo, TodoAdmin)