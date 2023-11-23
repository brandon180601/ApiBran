# tests/test_models.py

import pytest
from api.models import Preguntas  # Ajusta la importación según la estructura de tu proyecto

@pytest.mark.django_db  # Marca la prueba para usar una base de datos de prueba
def test_preguntas_creation():
    pregunta = Preguntas.objects.create(
        descripcion='Descripción 1',
        descripcion1='Descripción 2',
        descripcion2='Descripción 3',
        descripcion3='Descripción 4',
        descripcion4='Descripción 5',
        descripcion5='Descripción 6',
        descripcion6='Descripción 7',
        descripcion7='Descripción 8',
        descripcion8='Descripción 9',
        descripcion9='Descripción 10',
        descripcion10='Descripción 11'
        # ... continúa con los campos restantes
    )

    assert pregunta.id_respuesta is not None  # Verifica si se creó la instancia correctamente
    assert pregunta.descripcion == 'Descripción 1'  # Verifica valores específicos
    # ... verifica otros campos y lógica en tu modelo
