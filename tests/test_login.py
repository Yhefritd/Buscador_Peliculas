# tests/test_login.py
import pytest
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from Buscador_Pelicula.views import login_view  # Asegúrate de que la importación sea correcta
from Buscador_Pelicula.models import Usuario  # Importar el modelo de Usuario de la aplicación

@pytest.fixture
def setup_usuario():
    """Fixture para crear un usuario para los tests"""
    usuario = Usuario.objects.create(
        nombre="Test User",
        email="testuser@example.com",
        contrasena="password123",  # Asegúrate de que esta sea la contraseña correcta para las pruebas
        rol="user"
    )
    return usuario

@pytest.fixture
def request_factory():
    """Fixture para crear una solicitud de prueba"""
    return RequestFactory()

def test_login_exitoso(request_factory, setup_usuario):
    """Prueba para un login exitoso"""
    request = request_factory.post(reverse('login'), {'correo': 'testuser@example.com', 'password': 'password123'})
    
    # Establecer sesión para la solicitud
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()
    
    # Ejecutar la vista
    response = login_view(request)
    
    # Verificar que la sesión se establezca correctamente
    assert response.status_code == 302  # Redirige al 'taquilla'
    assert response.url == reverse('taquilla')  # Verificamos que redirige a la página 'taquilla'
    assert 'usuario_id' in request.session  # Verificamos que se haya guardado el usuario en la sesión

def test_login_contrasena_incorrecta(request_factory, setup_usuario):
    """Prueba para el caso donde la contraseña es incorrecta"""
    request = request_factory.post(reverse('login'), {'correo': 'testuser@example.com', 'password': 'wrongpassword'})
    
    # Establecer sesión para la solicitud
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()
    
    # Ejecutar la vista
    response = login_view(request)
    
    # Verificar que la vista renderice 'index.html' con un mensaje de error
    assert response.status_code == 200
    assert 'Contraseña incorrecta' in response.content.decode()

def test_login_usuario_no_encontrado(request_factory):
    """Prueba para el caso donde el usuario no se encuentra"""
    request = request_factory.post(reverse('login'), {'correo': 'nonexistentuser@example.com', 'password': 'password123'})
    
    # Establecer sesión para la solicitud
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()
    
    # Ejecutar la vista
    response = login_view(request)
    
    # Verificar que la vista renderice 'index.html' con un mensaje de error
    assert response.status_code == 200
    assert 'Usuario no encontrado' in response.content.decode()
