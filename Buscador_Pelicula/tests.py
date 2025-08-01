# tests/test_views.py
import pytest
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from Buscador_Pelicula.views import login_view, logout_view, registro_view, taquilla, peliculas, series
from Buscador_Pelicula.models import Usuario

@pytest.fixture
def setup_usuario():
    return Usuario.objects.create(
        nombre="Yhefritd",
        email="huachomontes123.1@gmail.com",
        contrasena="123",
        rol="user"
    )

@pytest.fixture
def request_factory():
    return RequestFactory()

def test_login_exitoso(request_factory, setup_usuario):
    request = request_factory.post(reverse('login'), {'correo': 'huachomontes123.1@gmail.com', 'password': '123'})
    
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()
    
    response = login_view(request)
    
    assert response.status_code == 302
    assert response.url == reverse('taquilla')
    assert 'usuario_id' in request.session

def test_login_contrasena_incorrecta(request_factory, setup_usuario):
    request = request_factory.post(reverse('login'), {'correo': 'huachomontes123.1@gmail.com', 'password': 'wrongpassword'})
    
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()
    
    response = login_view(request)
    
    assert response.status_code == 200
    assert 'Contraseña incorrecta' in response.content.decode()

def test_login_usuario_no_encontrado(request_factory):
    request = request_factory.post(reverse('login'), {'correo': 'nonexistentuser@example.com', 'password': '123'})
    
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()
    
    response = login_view(request)
    
    assert response.status_code == 200
    assert 'Usuario no encontrado' in response.content.decode()

def test_logout_view(request_factory, setup_usuario):
    request = request_factory.get(reverse('logout'))
    request.session['usuario_id'] = setup_usuario.id_usuario
    
    response = logout_view(request)
    
    assert response.status_code == 302
    assert 'usuario_id' not in request.session

def test_registro_view(request_factory):
    request = request_factory.post(reverse('registro'), {'nombre': 'Nuevo Usuario', 'correo': 'newuser@example.com', 'password': 'newpassword123'})
    
    response = registro_view(request)
    
    assert response.status_code == 302
    assert Usuario.objects.filter(email='newuser@example.com').exists()

def test_registro_view_correo_ya_registrado(request_factory, setup_usuario):
    request = request_factory.post(reverse('registro'), {'nombre': 'Otro Usuario', 'correo': 'huachomontes123.1@gmail.com', 'password': 'newpassword123'})
    
    response = registro_view(request)
    
    assert response.status_code == 200
    assert 'El correo ya está registrado' in response.content.decode()

def test_taquilla_redirige_sin_usuario(request_factory):
    request = request_factory.get(reverse('taquilla'))
    
    response = taquilla(request)
    
    assert response.status_code == 302
    assert response.url == reverse('index')

def test_peliculas_redirige_sin_usuario(request_factory):
    request = request_factory.get(reverse('peliculas'))
    
    response = peliculas(request)
    
    assert response.status_code == 302
    assert response.url == reverse('index')

def test_series_redirige_sin_usuario(request_factory):
    request = request_factory.get(reverse('series'))
    
    response = series(request)
    
    assert response.status_code == 302
    assert response.url == reverse('index')
