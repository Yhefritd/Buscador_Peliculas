from django.shortcuts import render

def index(request):
    return render(request, 'taquilla.html')

def pagina_index(request):
    return render(request, 'index.html')

def peliculas(request):
    return render(request, 'Peliculas.html')

from django.shortcuts import render

def index(request):
    return render(request, 'taquilla.html')

def peliculas(request):
    return render(request, 'Peliculas.html')

def series(request):
    return render(request, 'Series.html')   # <-- Aquí con S mayúscula
