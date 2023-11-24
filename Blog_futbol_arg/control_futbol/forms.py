from django import forms
from control_futbol.models import Articulo

class JugadorFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=256)
    club = forms.CharField(required=True, max_length=256)
    altura = forms.CharField(max_length=64)
    peso = forms.IntegerField(max_value=200)

class ClubFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    ubicacion = forms.CharField(required=True, max_length=256)

class EntrenadorFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=256)
    club = forms.CharField(required=True, max_length=256)

class ArticuloFormulario(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'subtitulo', 'cuerpo']


# class ArticuloFormulario(forms.Form):
#     autor = forms.CharField(required=True, max_length=256)
#     titulo = forms.CharField(required=True, max_length=256)
#     subtitulo = forms.CharField(required=True, max_length=256)
#     cuerpo = forms.TextInput(required=True)

