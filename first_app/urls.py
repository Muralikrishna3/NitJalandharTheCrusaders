from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='queue_list'),
    path('update/', views.updateLength, name='length'),
    path('start/', views.startFunction, name='start'),
    path('stop/', views.stopFunction, name='stop'),
]
