from django.shortcuts import render

def index(request):
    return render(request, 'taquilla.html')

def pagina_index(request):
    return render(request, 'index.html')
