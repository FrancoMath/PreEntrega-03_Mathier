from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Cliente, Pedido_Basico

#from django.contrib.auth.decorators import login_required
#@login_required

def inicio(request):
    return render(request, "AppCorrea/index.html")



def productos(request):
    if request.method == 'POST':
        producto = Producto(nombre=request.POST['nombre'], precio=request.POST['precio'],
        descripcion=request.POST['descripcion'], en_stock=request.POST['en_stock'], 
        en_promocion=request.POST['en_promocion'], )
        producto.save()
        return render (request, "AppCorrea/index.html")
 
    return render(request,"AppCorrea/cargar_productos.html")


def clientes(request):
    if request.method == 'POST':
        cliente = Cliente(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
        direccion=request.POST['direccion'], email=request.POST['email'], 
        telefono=request.POST['telefono'], )
        cliente.save()
        return render (request, "AppCorrea/index.html")
 
    return render(request,"AppCorrea/cargar_clientes.html")


def pedidos_basicos(request):
    if request.method == 'POST':
        pedido_basico = Pedido_Basico(cliente_pedido=request.POST['cliente_pedido'], 
        fecha_pedido=request.POST['fecha_pedido'],
        horario_entrega=request.POST['horario_entrega'], detalle_pedido=request.POST['detalle_pedido'])
        pedido_basico.save()
        return render (request, "AppCorrea/index.html")
 
    return render(request,"AppCorrea/cargar_pedidos.html")


# def pedidos(request):
#     return render(request, "AppCorrea/cargar_pedidos.html")

def buscar_pedidos(request):
    return render(request, "AppCorrea/buscar_pedidos.html")


def buscar(request):
    if request.GET["fecha_pedido"]:
        fecha_pedido = request.GET['fecha_pedido']
        pedidos_basicos = Pedido_Basico.objects.filter(fecha_pedido__icontains=fecha_pedido)

        return render(request, "AppCorrea/leer_pedidos.html", {"pedidos_basicos":pedidos_basicos, 
        "fecha_pedido":fecha_pedido})
    
    else:
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)
    
    
    
    # respuesta = f"Estoy buscando pedidos con fecha: {request.GET['fecha_pedido']}"
    # return HttpResponse(respuesta)





def leer_productos(request):
    productos = Producto.objects.all()
    contexto = {"productos":productos}
    return render(request, "AppCorrea/leer_productos.html", contexto)
