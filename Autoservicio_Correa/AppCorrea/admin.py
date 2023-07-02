from django.contrib import admin
from .models import Cliente, Promocion, Comentario, MiPedido


admin.site.register(Cliente)
admin.site.register(Promocion)
admin.site.register(Comentario)
admin.site.register(MiPedido)
# admin.site.register(Pedido)
# admin.site.register(DetallePedido)