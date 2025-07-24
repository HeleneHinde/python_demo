"""
Configuration WSGI pour le projet python_demo1

Ce fichier expose l'application Django compatible WSGI.
Il est utilisé par le serveur de développement et les serveurs de production.

Pour plus d'informations sur ce fichier, voir :
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Configuration de la variable d'environnement pour les paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_demo1.settings')

# Création de l'application WSGI
application = get_wsgi_application()
