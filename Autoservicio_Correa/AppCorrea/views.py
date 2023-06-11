from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppCorrea/index.html")

def productos(request):
    return HttpResponse("Vista productos")

def clientes(request):
    return HttpResponse("Vista clientes")

def pedidos(request):
    return HttpResponse("Vista pedidos")



