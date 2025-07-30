import requests
from django.http import JsonResponse

def conectar_omdb(request):
    API_KEY = '4a810142' 
    url = f'https://www.omdbapi.com/?apikey={API_KEY}&s=batman'

    response = requests.get(url)
    data = response.json()

    return JsonResponse(data)
