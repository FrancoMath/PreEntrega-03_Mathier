from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto, Cliente, Pedido, Promocion, MiPedido
from .forms import FormularioMiPedido

# Inicio
def inicio(request):
    return render(request, "AppCorrea/index.html")


# Promociones
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


# Pedidos
def cargar_mis_pedido(request):
    if request.method == 'POST':
        form = FormularioMiPedido(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.user = request.user
            pedido.save()
            return redirect('Leer solo mis Pedidos') #cambiar esto para que vuelva la vista correcta
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
    
