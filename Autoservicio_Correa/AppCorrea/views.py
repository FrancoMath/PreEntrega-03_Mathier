from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppCorrea/index.html")

def productos(request):
    return render(request, "AppCorrea/cargar_productos.html")

def clientes(request):
    return render(request, "AppCorrea/cargar_clientes.html")

def pedidos(request):
    return render(request, "AppCorrea/cargar_pedidos.html")

def buscar_productos(request):
    return render(request, "AppCorrea/buscar_productos.html")

