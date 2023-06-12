from django.urls import path
from AppCorrea import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cargar_clientes/', views.clientes, name="Cargar Clientes"),
    path('cargar_pedidos/', views.pedidos_basicos, name="Cargar Pedidos"),
    path('buscar_productos/', views.buscar_productos, name="Buscar Productos"),
    path('leer_productos/', views.leer_productos, name="Leer Productos"),
    path('cargar_productos/', views.productos, name="Cargar Productos"),
]