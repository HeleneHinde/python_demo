"""
Vues pour les pages statiques du site

Ce module contient les vues pour les pages qui ne dépendent pas
des modèles de données : page d'accueil, à propos, etc.
Ces pages sont généralement statiques ou avec peu de logique.
"""

from django.shortcuts import render
from django.http import HttpResponse


def accueil(request):
    """
    Vue d'accueil simple
    
    Cette vue affiche la page d'accueil du site. Pour l'instant,
    elle retourne du HTML directement via HttpResponse.
    
    Note: Dans une vraie application, on utiliserait plutôt
    un template HTML pour la page d'accueil.
    
    Args:
        request (HttpRequest): L'objet requête HTTP de Django
        
    Returns:
        HttpResponse: La page d'accueil en HTML
    """
    # Retour direct de HTML (méthode simple pour démonstration)
    # Dans un vrai projet, on utiliserait render() avec un template
    return render(request, 'blog/index.html')


def about(request):
    """
    Vue à propos avec template
    
    Cette vue affiche la page "À propos" du site en utilisant
    un template HTML. Elle montre comment passer des données
    du contrôleur (vue) vers la présentation (template).
    
    Args:
        request (HttpRequest): L'objet requête HTTP de Django
        
    Returns:
        HttpResponse: La page "À propos" générée à partir du template
    """
    # Préparation des données à envoyer au template
    # Le dictionnaire 'context' contient toutes les variables
    # qui seront disponibles dans le template HTML
    context = {
        'titre': 'À propos de nous',
        'description': 'Ceci est une page créée avec Django et un template HTML'
    }
    
    # Rendu du template avec les données
    # render() combine le template et le contexte pour générer la page finale
    return render(request, 'blog/about.html', context)
