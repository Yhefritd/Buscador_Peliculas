
from django.db import models
# from django.contrib.auth.models import AbstractUser  # Descomenta para usar el sistema de usuarios de Django

# class Usuario(AbstractUser):
#     ROL_CHOICES = [
#         ("admin", "Admin"),
#         ("user", "User"),
#     ]
#     rol = models.CharField(max_length=10, choices=ROL_CHOICES)
#     # El resto de campos (email, password, etc.) ya están incluidos en AbstractUser
#     def __str__(self):
#         return self.username

class Usuario(models.Model):
    ROL_CHOICES = [
        ("admin", "Admin"),
        ("user", "User"),
    ]
    id_usuario = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=128)
    rol = models.CharField(max_length=10, choices=ROL_CHOICES)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

class Obra(models.Model):
    titulo = models.CharField(max_length=200)
    anio = models.SmallIntegerField()
    descripcion = models.TextField()
    imagen_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

class Pelicula(Obra):
    pass

class Serie(Obra):
    pass
