from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def jongro(request):
    return render(request, 'jongro.html')