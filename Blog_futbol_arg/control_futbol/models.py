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

class Blog(models.Model):
    autor = models.CharField(max_length=256)
    contenido = models.CharField(max_length=1000)