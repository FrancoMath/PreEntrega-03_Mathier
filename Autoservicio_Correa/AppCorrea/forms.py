from django import forms
from django.contrib.auth.models import User 

from .models import Comentario, MiPedido, Promocion


class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'apellido', 'mensaje')
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class FormularioMiPedido(forms.ModelForm):
    class Meta:
        model = MiPedido
        fields = ('nombre_apellido', 'fecha_pedido', 'horario_entrega', 'lugar_entrega', 'detalle_pedido')
        widgets = {'nombre_apellido': forms.TextInput(attrs={'class': 'form-control'}),
        'fecha_pedido': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'horario_entrega': forms.TextInput(attrs={'class': 'form-control'}),
        'lugar_entrega': forms.TextInput(attrs={'class': 'form-control'}),
        'detalle_pedido' : forms.Textarea(attrs={'class': 'form-control'}),
        }
