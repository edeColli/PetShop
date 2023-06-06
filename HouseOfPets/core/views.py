from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def sobre(request):
    return render(request, 'about.html')

@login_required
def sair(request):
    logout(request)
    return redirect('/')