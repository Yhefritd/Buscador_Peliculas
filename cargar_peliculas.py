import os
import django
import json

# Configura el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Buscador_Peliculas.settings')
django.setup()

from NuestraApp.models import Pelicula

# Cargar datos desde JSON
with open('peliculas.json', 'r', encoding='utf-8') as archivo:
    data = json.load(archivo)

# Insertar películas en la base de datos
for item in data:
    Pelicula.objects.create(
        titulo=item['titulo'],
        genero=item['genero'],
        anio=item['anio'],
        descripcion=item['descripcion'],
        imagen_url=item['imagen_url']
    )

print("Películas cargadas con éxito.")
