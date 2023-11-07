from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from control_futbol.models import Jugador, Club, Entrenador
from control_futbol.forms import JugadorFormulario, ClubFormulario, EntrenadorFormulario


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

def listar_clubes(request):
    contexto = {
        "clubes": Club.objects.all(),
    }
    http_response = render(
        request = request,
        template_name = 'control_futbol/lista_clubes.html',
        context=contexto,
    )
    return http_response

def crear_jugadores(request):
    if request.method == "POST":
        formulario = JugadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            club = data["club"]
            altura = data["altura"]
            peso = data["peso"]

            jugador = Jugador(nombre=nombre, apellido=apellido, club=club, altura=altura, peso=peso)
            jugador.save()

            url_exitosa = reverse('lista_jugadores')
            return redirect(url_exitosa)
    else:
        formulario=JugadorFormulario()
        
    http_response = render(
        request=request,
        template_name='control_futbol/agregar_jugadores.html',
        context={'formulario': formulario}
    )
    return http_response


def crear_clubes(request):
    if request.method == "POST":
        formulario = ClubFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            ubicacion = data["ubicacion"]

            jugador = Club(nombre=nombre, ubicacion=ubicacion)
            jugador.save()

            url_exitosa = reverse('lista_clubes')
            return redirect(url_exitosa)
    else:
        formulario=ClubFormulario()
        
    http_response = render(
        request=request,
        template_name='control_futbol/agregar_clubes.html',
        context={'formulario': formulario}
    )
    return http_response