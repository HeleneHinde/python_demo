"""
Configuration des URLs pour l'application blog

Ce fichier définit toutes les routes de l'application blog.
Il importe les URLs depuis le package urls/ pour une meilleure organisation.
"""

from django.urls import path, include

# Import des vues pour les routes simples
from .views import home_views, article_views

# Configuration des routes de l'application blog
urlpatterns = [
    # === PAGES D'ACCUEIL ===
    path('', home_views.accueil, name='accueil'),
    path('about/', home_views.about, name='about'),
    
    # === ARTICLES ===
    path('articles/', article_views.liste_articles, name='liste_articles'),
    path('article/<int:article_id>/', article_views.detail_article, name='detail_article'),
    path('categorie/<int:categorie_id>/', article_views.articles_par_categorie, name='articles_categorie'),
]
