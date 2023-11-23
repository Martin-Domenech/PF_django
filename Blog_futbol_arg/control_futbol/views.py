from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from control_futbol.models import Jugador, Club, Entrenador, Articulo
from control_futbol.forms import JugadorFormulario, ClubFormulario, EntrenadorFormulario, ArticuloFormulario


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

def listar_entrenadores(request):
    contexto = {
        "entrenadores": Entrenador.objects.all(),
    }
    http_response = render(
        request = request,
        template_name = 'control_futbol/lista_entrenadores.html',
        context=contexto,
    )
    return http_response


def listar_articulo(request):
    contexto = {
        "articulos": Articulo.objects.all(),
    }
    http_response = render(
        request = request,
        template_name = 'control_futbol/lista_articulos.html',
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

            club = Club(nombre=nombre, ubicacion=ubicacion)
            club.save()

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

 
def crear_entrenadores(request):
    if request.method == "POST":
        formulario = EntrenadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            club = data["club"]

            entrenador = Entrenador(nombre=nombre, apellido=apellido, club=club)
            entrenador.save()

            url_exitosa = reverse('lista_entrenadores')
            return redirect(url_exitosa)
    else:
        formulario=EntrenadorFormulario()
        
    http_response = render(
        request=request,
        template_name='control_futbol/agregar_entrenadores.html',
        context={'formulario': formulario}
    )
    return http_response

def crear_articulos(request):
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            autor = data["autor"]
            cuerpo = data["cuerpo"]
            titulo = data["titulo"]
            subtitulo = data["subtitulo"]
            fecha = data["fecha"]


            articulo = Articulo(autor=autor, cuerpo=cuerpo, titulo=titulo, subtitulo=subtitulo, fecha=fecha)
            articulo.save()

            url_exitosa = reverse('lista_articulos')
            return redirect(url_exitosa)
    else:
        formulario=ArticuloFormulario()
        
    http_response = render(
        request=request,
        template_name='control_futbol/agregar_articulos.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_jugadores(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        jugadores = Jugador.objects.filter(
            Q(nombre__contains=busqueda) | Q(apellido__contains=busqueda)
        )
        contexto = {
            "jugadores": jugadores,
        }
    http_response = render(
        request=request,
        template_name='control_futbol/lista_jugadores.html',
        context=contexto,
    )
    return http_response    

def eliminar_articulo(request, id):
   articulo = Articulo.objects.get(id=id)
   if request.method == "POST":
       articulo.delete()
       url_exitosa = reverse('lista_articulos')
       return redirect(url_exitosa)
   
def editar_articulo(request, id):
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            articulo.autor = data['autor']
            articulo.cuerpo = data['cuerpo']
            articulo.titulo = data['titulo']
            articulo.subtitulo = data['subtitulo']
            articulo.fecha = data['fecha']
  
            articulo.save()
            url_exitosa = reverse('lista_articulos')
            return redirect(url_exitosa)
        else:  # GET
            inicial = {
                'autor': articulo.autor,
                'cuerpo': articulo.cuerpo,
                'titulo': articulo.titulo,
                'subtitulo': articulo.subtitulo,
                'fecha': articulo.fecha,
            }
        formulario = ArticuloFormulario(initial=inicial)
    return render(
        request=request,
        template_name='control_futbol/agregar_articulos.html',
        context={'formulario': formulario},
    )
