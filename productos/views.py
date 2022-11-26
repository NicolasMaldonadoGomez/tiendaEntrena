from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto


def index(request):
    productos = Producto.objects.all()
    return render (request, 'index.html',{'productos':productos})


def nuevo(request):
    return HttpResponse("¿Cual es tu nuevo producto?")
    
