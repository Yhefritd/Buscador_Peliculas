
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('correo')
        password = request.POST.get('password')
        try:
            usuario = Usuario.objects.get(email=email)
            if usuario.contrasena == password:
                request.session['usuario_id'] = usuario.id_usuario
                return redirect('taquilla')
            else:
                return render(request, 'index.html', {'error': 'Contraseña incorrecta'})
        except Usuario.DoesNotExist:
            return render(request, 'index.html', {'error': 'Usuario no encontrado'})
    return render(request, 'index.html')

def logout_view(request):
    request.session.flush()
    return redirect('index')

def registro_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('correo')
        password = request.POST.get('password')
        # Puedes agregar validaciones aquí
        if Usuario.objects.filter(email=email).exists():
            return render(request, 'registro.html', {'error': 'El correo ya está registrado'})
        usuario = Usuario(nombre=nombre, email=email, contrasena=password, rol='user')
        usuario.save()
        return redirect('index')
    return render(request, 'registro.html')

def taquilla(request):
    if not request.session.get('usuario_id'):
        return redirect('index')
    return render(request, 'taquilla.html')

def peliculas(request):
    if not request.session.get('usuario_id'):
        return redirect('index')
    return render(request, 'Peliculas.html')

def series(request):
    if not request.session.get('usuario_id'):
        return redirect('index')
    return render(request, 'Series.html')
