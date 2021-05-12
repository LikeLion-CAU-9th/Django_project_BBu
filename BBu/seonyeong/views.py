from django.shortcuts import render
from jiwon import views
# Create your views here.
def home(request):
    return render(request, 'home.html')

def jongro(request):
    return render(request, 'jongro.html')