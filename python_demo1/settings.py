"""
Configuration Django pour le projet python_demo1

Ce fichier contient tous les paramètres de configuration pour l'application Django.
Il définit la base de données, les applications installées, les middlewares,
et toutes les autres options nécessaires au fonctionnement du projet.

Généré par 'django-admin startproject' avec Django 5.2.4.

Pour plus d'informations sur ce fichier, voir :
https://docs.djangoproject.com/en/5.2/topics/settings/

Pour la liste complète des paramètres et leurs valeurs, voir :
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# === CONFIGURATION DES CHEMINS ===
# Chemin de base du projet : répertoire parent du fichier settings.py
BASE_DIR = Path(__file__).resolve().parent.parent


# === CONFIGURATION DE SÉCURITÉ ===
# ATTENTION : Cette clé secrète doit être gardée secrète en production !
# Elle est utilisée pour les signatures cryptographiques dans Django
SECRET_KEY = 'django-insecure-=6juf-xn8s81$(4$1wdvlbr-@+^@&_ec$x$te&2@+f+no%n=2z'

# Mode debug : DOIT être à False en production
# En mode debug, Django affiche des informations détaillées sur les erreurs
DEBUG = True

# Hôtes autorisés à accéder à l'application
# En production, spécifier les domaines autorisés : ['monsite.com', 'www.monsite.com']
ALLOWED_HOSTS = []


# === DÉFINITION DES APPLICATIONS ===
# Liste des applications Django installées dans ce projet
INSTALLED_APPS = [
    # Applications Django par défaut
    'django.contrib.admin',          # Interface d'administration
    'django.contrib.auth',           # Système d'authentification
    'django.contrib.contenttypes',   # Framework de types de contenu
    'django.contrib.sessions',       # Framework de sessions
    'django.contrib.messages',       # Framework de messages
    'django.contrib.staticfiles',    # Gestion des fichiers statiques
    
    # Applications personnalisées
    'blog',                          # Notre application de blog
]

# === MIDDLEWARES ===
# Liste des middlewares Django (traitement des requêtes/réponses)
# L'ordre est important ! Chaque middleware traite la requête dans l'ordre
# et la réponse dans l'ordre inverse
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',        # Sécurité HTTPS
    'django.contrib.sessions.middleware.SessionMiddleware', # Gestion des sessions
    'django.middleware.common.CommonMiddleware',            # Fonctionnalités communes
    'django.middleware.csrf.CsrfViewMiddleware',           # Protection CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Authentification
    'django.contrib.messages.middleware.MessageMiddleware',    # Messages flash
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protection clickjacking
]

# === CONFIGURATION DES URLS ===
# Fichier racine de configuration des URLs
ROOT_URLCONF = 'python_demo1.urls'

# === CONFIGURATION DES TEMPLATES ===
# Configuration du système de templates Django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],                    # Répertoires additionnels de templates
        'APP_DIRS': True,              # Chercher les templates dans les apps
        'OPTIONS': {
            'context_processors': [     # Processeurs de contexte globaux
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# === CONFIGURATION WSGI ===
# Application WSGI pour le déploiement
WSGI_APPLICATION = 'python_demo1.wsgi.application'


# === CONFIGURATION DE LA BASE DE DONNÉES ===
# Configuration de la base de données (SQLite par défaut pour le développement)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',        # Moteur de base de données
        'NAME': BASE_DIR / 'db.sqlite3',               # Chemin vers le fichier SQLite
    }
}

# Pour PostgreSQL en production, utiliser quelque chose comme :
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'nom_de_la_base',
#         'USER': 'utilisateur',
#         'PASSWORD': 'mot_de_passe',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


# === VALIDATION DES MOTS DE PASSE ===
# Validateurs pour s'assurer que les mots de passe sont sécurisés
AUTH_PASSWORD_VALIDATORS = [
    {
        # Vérifie que le mot de passe n'est pas trop similaire aux informations personnelles
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        # Vérifie que le mot de passe contient au moins 8 caractères
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        # Vérifie que le mot de passe n'est pas dans une liste de mots de passe courants
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        # Vérifie que le mot de passe n'est pas entièrement numérique
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# === INTERNATIONALISATION ===
# Configuration de la langue et de la localisation

# Code de langue principal (français)
LANGUAGE_CODE = 'fr-fr'

# Fuseau horaire
TIME_ZONE = 'Europe/Paris'

# Utiliser les traductions Django
USE_I18N = True

# Utiliser les formats de date/heure localisés
USE_TZ = True


# === FICHIERS STATIQUES (CSS, JavaScript, Images) ===
# Configuration pour servir les fichiers statiques
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# URL de base pour les fichiers statiques
STATIC_URL = 'static/'

# Répertoire où collecter tous les fichiers statiques pour la production
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Répertoires supplémentaires où chercher les fichiers statiques
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]


# === TYPE DE CLÉ PRIMAIRE PAR DÉFAUT ===
# Type de champ à utiliser pour les clés primaires auto-générées
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# === CONFIGURATION DU LOGGING (OPTIONNEL) ===
# Configuration pour enregistrer les logs de l'application
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': BASE_DIR / 'django.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#     },
# }


# === CONFIGURATION EMAIL (POUR LA PRODUCTION) ===
# Configuration pour l'envoi d'emails
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'votre-email@gmail.com'
# EMAIL_HOST_PASSWORD = 'votre-mot-de-passe'


# === CONFIGURATION CACHE (POUR LA PRODUCTION) ===
# Configuration du cache pour améliorer les performances
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.redis.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/1',
#     }
# }
