from django.urls import path


app_name = 'pages'
urlpatterns = [

    path('index/', views.index, name='index'),

]