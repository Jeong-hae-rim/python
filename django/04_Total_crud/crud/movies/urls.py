from django.urls import path
from . import views


app_name='movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'), 
]
