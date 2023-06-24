from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Promocion, Pedido_Basico, Comentario
from .forms import FormularioComentario
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PromocionListView(ListView):
    model = Promocion
    template_name = "AppCorrea/leer_promociones.html"

class PromocionDetailView(LoginRequiredMixin, DetailView):
    model = Promocion
    template_name = "AppCorrea/detalle_promocion.html"

class PromocionUpdateView(UpdateView):
    model = Promocion
    success_url = reverse_lazy("Leer Promociones")
    fields = ["id", "fecha_inicio", "fecha_fin", "titulo_promo", "descripcion_promo",
    "precio_promo", "estado_promo"]
    template_name = "AppCorrea/editar_promocion.html"

class PromocionDeleteView(DeleteView):
    model = Promocion
    success_url = reverse_lazy("Leer Promociones")
    template_name = 'AppCorrea/eliminar_promocion.html'


class Pedido_BasicoListView(ListView):
    model = Pedido_Basico
    template_name = "AppCorrea/leer_mis_pedidos.html"


class Pedido_BasicoDetailView(LoginRequiredMixin, DetailView):
    model = Pedido_Basico
    template_name = "AppCorrea/detalle_pedido.html"



class Pedido_BasicoUpdateView(UpdateView):
    model = Pedido_Basico
    success_url = reverse_lazy("Leer Mis Pedidos")
    fields = ["id", "fecha_pedido", "horario_entrega", "detalle_pedido", 
    "estado_pedido",]
    template_name = "AppCorrea/editar_pedido.html"


class Pedido_BasicoDeleteView(DeleteView):
    model = Pedido_Basico
    success_url = reverse_lazy("Leer Mis Pedidos")
    template_name = 'AppCorrea/eliminar_pedido.html'



class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'AppCorrea/comentario.html'
    success_url = reverse_lazy('Leer Promociones')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)