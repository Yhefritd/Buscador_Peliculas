import requests
from django.http import JsonResponse
from django.shortcuts import render

# conecta a la API de OMDB
def conectar_omdb(request):
    API_KEY = '4a810142'
    url = f'https://www.omdbapi.com/?apikey={API_KEY}&s=batman'

    response = requests.get(url)
    data = response.json()

    return JsonResponse(data)

# Funciones del main (respetadas)
def index(request):
    return render(request, 'taquilla.html')

def pagina_index(request):
    return render(request, 'index.html')
