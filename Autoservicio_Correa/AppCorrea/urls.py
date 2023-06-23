from django.urls import path
from AppCorrea import views, class_views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('index/', views.inicio, name="Inicio"),
    path('cargar_clientes/', views.clientes, name="Cargar Clientes"),
    path('cargar_pedidos/', views.pedidos_basicos, name="Cargar Pedidos"),
    path('buscar_pedidos/', views.buscar_pedidos, name="Buscar Pedidos"),
    path('leer_productos/', views.leer_productos, name="Leer Productos"),
    path('cargar_productos/', views.productos, name="Cargar Productos"),
    path('cargar_promocion/', views.promociones, name="Cargar Promociones"),
    path('leer_promociones/', views.leer_promociones, name="Leer Promociones"),
    path('buscar/', views.buscar),
]


# URL's basadas en clases
urlpatterns += [
    path('editar_promocion/<pk>/', class_views.PromocionUpdateView.as_view(), name="Editar Promocion"),
    path('eliminar_promocion/<pk>/', class_views.PromocionDeleteView.as_view(), name="Eliminar Promocion"),
    path('detalle_promocion/<pk>/', class_views.PromocionDetailView.as_view(), name="Detalle Promocion"),
]