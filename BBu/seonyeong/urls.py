import seonyeong.views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',seonyeong.views.home, name = "home"),
    path('jongro/', seonyeong.views.jongro, name = 'jongro'),
]
