from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('twit/', views.twit, name='twit'),
    path('reply/', views.reply, name='reply'),
]
