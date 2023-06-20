from django.urls import path
from AppCorrea import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('index/', views.inicio, name="Inicio"),
    path('cargar_clientes/', views.clientes, name="Cargar Clientes"),
    path('cargar_pedidos/', views.pedidos_basicos, name="Cargar Pedidos"),
    path('buscar_pedidos/', views.buscar_pedidos, name="Buscar Pedidos"),
    path('leer_productos/', views.leer_productos, name="Leer Productos"),
    path('cargar_productos/', views.productos, name="Cargar Productos"),
    path('buscar/', views.buscar),
]