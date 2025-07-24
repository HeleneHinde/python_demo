"""
Configuration des URLs pour le projet python_demo1

Ce fichier définit les routes principales du projet.
Il inclut les URLs de l'application blog et l'interface d'administration.
"""

from django.contrib import admin
from django.urls import path, include

# Configuration des routes principales du projet
urlpatterns = [
    # Interface d'administration Django
    path('admin/', admin.site.urls),
    
    # Routes de l'application blog (toutes les pages du site)
    path('', include('blog.urls')),
]
