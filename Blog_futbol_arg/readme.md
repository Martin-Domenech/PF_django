# FutbolARG

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Instrucciones para entrar al panel aministrativo de Django
+ En consola, crear un superuser:
```
python manage.py createsuperuser
```
+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```

## Instrucciones para prender el servidor
+ En la consola entrar a la carpeta Blog_futbol_arg mediante el comando:
```
cd Blog_futbol_arg
```
+ Luego prender el servidor:
```
python manage.py runserver
```

# Superusuario de pruebas
username: admin
contraseña: qwer1234

# Funcionalidades
En la pagina se muestran en tablas los jugadores, entrenadores y clubes que hayan sido agregados por el usuario en 
la base de datos. Tambien en la seccion Jugadores se puede filtrar por nombre o apellido.