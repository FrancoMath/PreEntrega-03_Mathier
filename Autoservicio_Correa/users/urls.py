from django.urls import path
from users import views



urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', views.Logout.as_view(), name='Logout'),
    path('perfil/editar/', views.editar_perfil, name='Editar_perfil'),
    path('perfil/', views.mostrar_perfil, name='Mostrar_perfil'),
    path('perfil/cambiar_password/', views.CambiarPassword.as_view(), name='Cambiar_password'),
    path('perfil/eliminar/<int:pk>/', views.EliminarPerfil.as_view(), name='Eliminar_perfil'),
]