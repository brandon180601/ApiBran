import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'APIBRANDON.settings')  # Reemplaza 'tuproyecto.settings' con la ruta correcta a tu archivo settings.py

application = get_wsgi_application()
