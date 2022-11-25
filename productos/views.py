from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola, Django")


def nuevo(request):
    return HttpResponse("¿Cual es tu nuevo producto?")
    
