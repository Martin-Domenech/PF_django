from django.db import models

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
    autor = models.CharField(max_length=256)
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.CharField(max_length=1200)
    fecha = models.CharField(max_length=64)