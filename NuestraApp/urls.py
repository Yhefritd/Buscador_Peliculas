"""
URL configuration for NuestraApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Buscador_Pelicula import views  # Importa las vistas de la app directamente

urlpatterns = [
    path('', views.index, name='index'),                    # Taquilla.html
    path('peliculas/', views.peliculas, name='peliculas'),  # Peliculas.html
    path('series/', views.series, name='series'),            # Series.html
]