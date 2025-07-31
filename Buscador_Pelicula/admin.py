from django.contrib import admin
from .models import Pelicula

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'anio', 'genero']  # Asegúrate de que estos campos existen en tu modelo
