from django.urls import path
from control_futbol.views import (
    listar_jugadores, crear_jugadores, listar_clubes, crear_clubes, listar_entrenadores,
     crear_entrenadores, buscar_jugadores, listar_articulo, crear_articulos, eliminar_articulo, editar_articulo
)

urlpatterns = [
    path("jugadores/", listar_jugadores, name="lista_jugadores"),
    path("agregar-jugadores/",  crear_jugadores, name="agregar_jugadores"),
    path("clubes/",  listar_clubes, name="lista_clubes"),
    path("agregar-clubes/",  crear_clubes, name="agregar_clubes"),
    path("entrenadores/",  listar_entrenadores, name="lista_entrenadores"),
    path("agregar-entrenadores/",  crear_entrenadores, name="agregar_entrenadores"),
    path("buscar-jugadores/",  buscar_jugadores, name="buscar_jugadores"),
    path("articulos/",  listar_articulo, name="lista_articulos"),
    path("agregar-articulos/",  crear_articulos, name="agregar_articulos"),
    path("eliminar-articulo/<int:id>",  eliminar_articulo, name="eliminar_articulo"),
    path("editar-articulo/<int:id>",  editar_articulo, name="editar_articulo"),
]