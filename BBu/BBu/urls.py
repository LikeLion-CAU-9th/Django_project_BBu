import seonyeong.views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('seonyeong.urls')),
    path('', include('jiwon.urls') ),
    path('', include('seolhui.urls')),
]