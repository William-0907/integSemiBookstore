from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/home.html',)

def login(request):
    return render(request, 'website/login.html',)

def register(request):
    return render(request, 'website/register.html',)