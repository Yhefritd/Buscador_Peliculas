from django.shortcuts import render

def index(request):
    return render(request, 'Peliculas.html')

def pagina_index(request):
    return render(request, 'Peliculas.html')

def series(request):
    return render(request, 'Series.html')
