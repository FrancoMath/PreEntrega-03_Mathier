from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Cliente, Pedido, Promocion, MiPedido
from .forms import FormularioMiPedido

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


def pedidos(request):
    if request.method == 'POST':
        pedido = Pedido(cliente_pedido=request.POST['cliente_pedido'], 
        fecha_pedido=request.POST['fecha_pedido'],
        horario_entrega=request.POST['horario_entrega'], detalle_pedido=request.POST['detalle_pedido'])
        pedido.save()
        return render (request, "AppCorrea/index.html")
 
    return render(request,"AppCorrea/cargar_pedido.html")



def promociones(request):
    if request.method == 'POST':
        imagen_promo = request.FILES.get('imagen_promo')
        if not imagen_promo:
            imagen_promo = 'imagenes_promo\promo_generica.png'
        
        promocion = Promocion(fecha_inicio=request.POST['fecha_inicio'], fecha_fin=request.POST['fecha_fin'],
        titulo_promo=request.POST['titulo_promo'], descripcion_promo=request.POST['descripcion_promo'], 
        precio_promo=request.POST['precio_promo'], estado_promo=request.POST['estado_promo'], 
        imagen_promo=imagen_promo)
        promocion.save()
        return render (request, "AppCorrea/index.html")
 
    return render(request,"AppCorrea/cargar_promocion.html")

def leer_promociones(request):
    promociones = Promocion.objects.all()
    contexto = {"promociones":promociones}
    return render(request, "AppCorrea/leer_promociones.html", contexto)


def leer_mis_pedidos(request):
    pedidos = Pedido.objects.all()
    contexto = {"pedidos":pedidos}
    return render(request, "AppCorrea/leer_mis_pedidos.html", contexto)


#pruebas
def cargar_mis_pedido(request):
    if request.method == 'POST':
        form = FormularioMiPedido(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.user = request.user
            pedido.save()
            return render(request,"AppCorrea/leer_solo_mis_pedidos.html") #cambiar esto para que vuelva la vista correcta
    else:
        form = FormularioMiPedido()
    return render(request, 'AppCorrea/cargar_mis_pedidos.html', {'form': form})


def leer_solo_mis_pedidos(request):
    pedidos = MiPedido.objects.filter(user=request.user)
    return render(request, 'AppCorrea/leer_solo_mis_pedidos.html', {'pedidos': pedidos})


def leer_todos_los_pedidos(request):
    pedidos = MiPedido.objects.all()
    contexto = {"pedidos":pedidos}
    return render(request, "AppCorrea/leer_todos_los_pedidos.html", contexto)


# def pedidos(request):
#     return render(request, "AppCorrea/cargar_pedidos.html")

def buscar_pedidos(request):
    return render(request, "AppCorrea/buscar_pedidos.html")


def buscar(request):
    if request.GET["fecha_pedido"]:
        fecha_pedido = request.GET['fecha_pedido']
        pedidos = MiPedido.objects.filter(fecha_pedido__icontains=fecha_pedido)

        return render(request, "AppCorrea/leer_todos_los_pedidos.html", {"pedidos":pedidos, 
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
