from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return HttpResponse('Login')

def cadastro(request):
    return render(request, 'cadastro.html')
