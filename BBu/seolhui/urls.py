import seolhui.views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('mapo/', seolhui.views.mapo, name = 'mapo'),
]
