from django.urls import path
from control_futbol.views import (
    listar_jugadores, crear_jugadores
)

urlpatterns = [
    path("jugadores/", listar_jugadores, name="lista_jugadores"),
    path("agregar-jugadores/",  crear_jugadores, name="agregar_jugadores"),
]