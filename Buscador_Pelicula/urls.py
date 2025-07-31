from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),              
    path('inicio/', views.pagina_index, name='inicio'), 
    path('peliculas/', views.listar_peliculas, name='listar_peliculas'),  # Asegúrate de que esta vista exista
]
