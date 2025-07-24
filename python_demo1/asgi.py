"""
Configuration ASGI pour le projet python_demo1

Ce fichier expose l'application Django compatible ASGI.
Il est utilisé pour les fonctionnalités asynchrones (WebSockets, etc.)

Pour plus d'informations sur ce fichier, voir :
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Configuration de la variable d'environnement pour les paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_demo1.settings')

# Création de l'application ASGI
application = get_asgi_application()
