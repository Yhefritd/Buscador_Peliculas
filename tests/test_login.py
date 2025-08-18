import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NuestraApp.settings')
import django
from django.core.management import call_command

django.setup()
from django.conf import settings
settings.ALLOWED_HOSTS.append('testserver')
call_command('migrate', run_syncdb=True, verbosity=0)

from django.urls import reverse
from django.test import Client, TestCase
from Buscador_Pelicula.models import Usuario

class LoginViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario = Usuario.objects.create(
            nombre="Test User",
            email="testuser@example.com",
            contrasena="password123",
            rol="user"
        )

    def test_login_exitoso(self):
        response = self.client.post(reverse('index'), {
            'correo': 'testuser@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('taquilla'))
        self.assertEqual(self.client.session['usuario_id'], self.usuario.id_usuario)

    def test_login_contrasena_incorrecta(self):
        response = self.client.post(reverse('index'), {
            'correo': 'testuser@example.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Contraseña incorrecta', response.content.decode())

    def test_login_usuario_no_encontrado(self):
        response = self.client.post(reverse('index'), {
            'correo': 'nonexistent@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Usuario no encontrado', response.content.decode())
