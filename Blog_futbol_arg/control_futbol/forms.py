from django import forms

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

class BlogFormulario(forms.Form):
    autor = forms.CharField(required=True, max_length=256)
    contenido = forms.CharField(required=True, max_length=1000)