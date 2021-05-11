import jiwon.views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('songpa/', jiwon.views.songpa, name = 'songpa'),
]
