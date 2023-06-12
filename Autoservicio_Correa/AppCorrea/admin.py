from django.contrib import admin
from .models import Producto, Cliente, Pedido_Basico

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Pedido_Basico)
# admin.site.register(Pedido)
# admin.site.register(DetallePedido)