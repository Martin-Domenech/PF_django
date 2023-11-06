from django.db import models

# Create your models here.

class club(models.Model):
    nombre = models.CharField(max_length=256)
    ubicacion = models.CharField(max_length=256)


class jugador(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=256)
    club = models.CharField(max_length=256)
    altura = models.IntegerField()
    peso = models.IntegerField()


class entrenador(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=256)
    club = models.CharField(max_length=256)
