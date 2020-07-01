from django.urls import path
from . import views

app_name = 'apis'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('search/<search_string>/', views.search, name='search'),
    path('<int:pk>/status/', views.status, name='status'),
    path('<int:pk>/download/', views.download, name='download'),
    path('<int:pk>/graph/', views.graph, name='graph'),
    path('ranking/', views.ranking, name='ranking'),
]

