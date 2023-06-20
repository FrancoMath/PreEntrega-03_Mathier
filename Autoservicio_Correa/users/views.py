from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, LogoutView

from users import models, forms


# Vista de Login
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppCorrea/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCorrea/index.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "AppCorrea/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})

# Vista de registro
def register(request):

    if request.method == 'POST':

        #form = UserCreationForm(request.POST)
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppCorrea/index.html" ,  {"mensaje":"Usuario Creado :)"})

    else:
        #form = UserCreationForm()       
        form = forms.UserRegisterForm()     

    return render(request,"users/register.html" ,  {"form":form})


# Editar perfiles
@login_required
def editar_perfil(request):
    usuario = request.user
    modelo_perfil, _ = models.Perfil.objects.get_or_create(user=usuario)
    if request.method == "POST":
        form = forms.EditarUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('first_name'):
                usuario.first_name = data.get('first_name')
            if data.get('last_name'):
                usuario.last_name = data.get('last_name')
            usuario.email = data.get('email') if data.get('email') else usuario.email


            modelo_perfil.save()
            usuario.save()
            return redirect("Mostrar_perfil")
        else:
            return render(request, 'users/editar_perfil.html', {'form': form})

    form = forms.EditarUsuarioForm(
        initial={
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,

        }
    )
    return render(request, 'users/editar_perfil.html', {'form': form})

# Mostrar pefiles
@login_required
def mostrar_perfil(request):
    return render(request, 'users/mostrar_perfil.html')


# Cambiar contraseña

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/cambiar_password.html'
    success_url = reverse_lazy("Mostrar_perfil")

class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'users/logout.html'

class EliminarPerfil(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("Inicio")
    template_name = 'users/eliminar_perfil.html'