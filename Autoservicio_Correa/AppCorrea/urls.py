from django.urls import path
from AppCorrea import views, class_views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('index/', views.inicio, name="Inicio"),
    path('buscar/', views.buscar),
    path('buscar_pedidos/', views.buscar_pedidos, name="Buscar Pedidos"),

    path('cargar_promocion/', views.promociones, name="Cargar Promociones"),
    path('leer_promociones/', views.leer_promociones, name="Leer Promociones"),

    path('leer_todos_los_pedidos/', views.leer_todos_los_pedidos, name="Leer Pedidos"),
    path('cargar_mis_pedidos/', views.cargar_mis_pedido, name='Cargar MIS Pedidos'),
    path('leer_solo_mis_pedidos/', views.leer_solo_mis_pedidos, name='Leer solo mis Pedidos')
]


# URL's basadas en clases
urlpatterns += [
    path('editar_promocion/<pk>/', class_views.PromocionUpdateView.as_view(), name="Editar Promocion"),
    path('eliminar_promocion/<pk>/', class_views.PromocionDeleteView.as_view(), name="Eliminar Promocion"),
    path('detalle_promocion/<pk>/', class_views.PromocionDetailView.as_view(), name="Detalle Promocion"),
    
    path('editar_pedido/<pk>/', class_views.PedidoUpdateView.as_view(), name="Editar Pedido"),
    path('eliminar_pedido/<pk>/', class_views.PedidoDeleteView.as_view(), name="Eliminar Pedido"),
    path('detalle_pedido/<pk>/', class_views.PedidoDetailView.as_view(), name="Detalle Pedido"),

    path('detalle_promocion/<int:pk>/comentario/', class_views.ComentarioPagina.as_view(), name='comentario'),
]