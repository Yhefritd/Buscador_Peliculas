from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='index'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('taquilla/', views.taquilla, name='taquilla'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('series/', views.series, name='series'),
]
