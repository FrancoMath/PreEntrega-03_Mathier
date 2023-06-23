from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Promocion
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