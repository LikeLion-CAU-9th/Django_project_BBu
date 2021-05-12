from django.shortcuts import render
from seonyeong import views
# Create your views here.

def songpa(request):
    return render(request, 'songpa.html')