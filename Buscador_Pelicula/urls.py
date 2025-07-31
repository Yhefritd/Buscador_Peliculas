from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),              
    path('inicio/', views.pagina_index, name='inicio')
      
      
]
