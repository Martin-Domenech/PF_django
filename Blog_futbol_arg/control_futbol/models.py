from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Club(models.Model):
    nombre = models.CharField(max_length=256)
    ubicacion = models.CharField(max_length=256)



class Jugador(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=256)
    club = models.CharField(max_length=256)
    altura = models.CharField(max_length=64)
    peso = models.IntegerField()



class Entrenador(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=256)
    club = models.CharField(max_length=256)



class Articulo(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)