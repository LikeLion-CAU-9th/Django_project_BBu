from django.shortcuts import render
from seonyeong import views
# Create your views here.

def mapo(request):
    return render(request, 'mapo.html')