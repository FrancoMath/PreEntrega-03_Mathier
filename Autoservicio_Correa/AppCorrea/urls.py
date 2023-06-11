from django.urls import path
from AppCorrea import views

urlpatterns = [
    path('', views.inicio),
    path('productos/', views.productos),
    path('clientes/', views.clientes),
    path('pedidos/', views.pedidos),
]