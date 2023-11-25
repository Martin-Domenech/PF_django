from django.test import TestCase
from control_futbol.models import Club

# Create your tests here.
class ClubTests(TestCase):

   def test_creacion_Club(self):
       # caso uso esperado
       club = Club(nombre="Titulo", ubicacion="Lugar")
       club.save()

       # Compruebo que el curso fue creado y la data fue guardad correctamente
       self.assertEqual(club.objects.count(), 1)
       self.assertEqual(club.nombre, "Titulo")
       self.assertEqual(club.ubicacion, "Lugar")

   def test_club_str(self):
       club = Club(nombre="Boca", ubicacion="La Boca")
       club.save()

       # Compruebo el str funciona como se desea
       self.assertEqual(club.__str__(), "Boca, La Boca")