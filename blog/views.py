from django.http import HttpResponse
from django.template import Template, context
from django.template import loader
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def servicios(request):
    return render(request, 'servicios.html', {})

def tienda(request):
    return render(request, 'tienda.html', {})