from django.contrib import admin
from .models import Producto, Cliente, Pedido, Promocion, Comentario

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Promocion)
admin.site.register(Comentario)
# admin.site.register(Pedido)
# admin.site.register(DetallePedido)