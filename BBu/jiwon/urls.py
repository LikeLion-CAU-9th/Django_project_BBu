import jiwon.views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',jiwon.views.home, name = "home"),
    path('songpa/', jiwon.views.songpa, name = 'songpa'),
]
