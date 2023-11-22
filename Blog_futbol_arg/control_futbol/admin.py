from django.contrib import admin

# Register your models here.
from control_futbol.models import Jugador, Entrenador, Club, Blog
admin.site.register(Jugador)
admin.site.register(Entrenador)
admin.site.register(Club)
admin.site.register(Blog)