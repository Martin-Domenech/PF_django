from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from control_futbol.models import Jugador, Club, Entrenador


# Create your views here.

def listar_jugadores(request):
    contexto = {
        "jugadores": Jugador.objects.all(),
    }
    http_response = render(
        request = request,
        template_name = 'control_futbol/lista_jugadores.html',
        context=contexto,
    )
    
    return http_response