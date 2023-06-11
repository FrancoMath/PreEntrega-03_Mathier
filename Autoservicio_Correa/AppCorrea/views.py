from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Vista inicio")

def productos(request):
    return HttpResponse("Vista productos")

def clientes(request):
    return HttpResponse("Vista clientes")

def pedidos(request):
    return HttpResponse("Vista pedidos")



