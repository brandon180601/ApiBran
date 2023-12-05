# APIDJANGO/APIBRANDON/api/tests/test_models.py
# APIDJANGO/APIBRANDON/api/models.py

from django.test import TestCase
from api.models import Registro  # Reemplaza 'your_app' con el nombre de tu aplicación Django
  # Ajusta la importación según la estructura real de tu proyecto

class RegistroTestCase(TestCase):
    def setUp(self):
        # Crea un registro de ejemplo para utilizar en las pruebas
        self.registro = Registro.objects.create(
            idRegistro=1,
            usuario='usuario_prueba',
            correo='usuario@prueba.com',
            password='password_prueba'
        )

    def test_registro_creado_correctamente(self):
        # Verifica si el registro se creó correctamente
        self.assertEqual(self.registro.idRegistro, 1)
        self.assertEqual(self.registro.usuario, 'usuario_prueba')
        self.assertEqual(self.registro.correo, 'usuario@prueba.com')
        self.assertEqual(self.registro.password, 'password_prueba')
