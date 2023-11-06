from django.urls import path
from control_futbol.views import (
    listar_jugadores
)

urlpatterns = [
    path("jugadores/", listar_jugadores, name="lista_jugadores")
]