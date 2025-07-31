from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    anio = models.IntegerField()
    descripcion = models.TextField()
    imagen_url = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
