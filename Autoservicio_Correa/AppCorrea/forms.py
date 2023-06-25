from django import forms
from django.contrib.auth.models import User 

from .models import Comentario


class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'apellido', 'mensaje')
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }