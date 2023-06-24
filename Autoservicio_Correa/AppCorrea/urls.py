from django.urls import path
from AppCorrea import views, class_views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('index/', views.inicio, name="Inicio"),
    path('cargar_clientes/', views.clientes, name="Cargar Clientes"),
    path('cargar_pedido/', views.pedidos_basicos, name="Cargar Pedido"),
    path('buscar_pedidos/', views.buscar_pedidos, name="Buscar Pedidos"),
    path('leer_productos/', views.leer_productos, name="Leer Productos"),
    path('cargar_productos/', views.productos, name="Cargar Productos"),
    path('cargar_promocion/', views.promociones, name="Cargar Promociones"),
    path('leer_promociones/', views.leer_promociones, name="Leer Promociones"),
    path('leer_mis_pedidos/', views.leer_mis_pedidos, name="Leer Mis Pedidos"),
    path('buscar/', views.buscar),
]


# URL's basadas en clases
urlpatterns += [
    path('editar_promocion/<pk>/', class_views.PromocionUpdateView.as_view(), name="Editar Promocion"),
    path('eliminar_promocion/<pk>/', class_views.PromocionDeleteView.as_view(), name="Eliminar Promocion"),
    path('detalle_promocion/<pk>/', class_views.PromocionDetailView.as_view(), name="Detalle Promocion"),
    
    path('editar_pedido/<pk>/', class_views.Pedido_BasicoUpdateView.as_view(), name="Editar Pedido"),
    path('eliminar_pedido/<pk>/', class_views.Pedido_BasicoDeleteView.as_view(), name="Eliminar Pedido"),
    path('detalle_pedido/<pk>/', class_views.Pedido_BasicoDetailView.as_view(), name="Detalle Pedido"),


]