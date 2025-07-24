"""
Vues pour la gestion des articles

Ce module contient toutes les vues (contrôleurs) liées aux articles :
- Liste des articles avec pagination
- Détail d'un article avec articles similaires
- Articles par catégorie

Les vues utilisent le système de templates Django pour l'affichage.
"""

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from ..models import Article, Categorie


def liste_articles(request):
    """
    Vue pour afficher la liste des articles publiés avec pagination
    
    Cette vue récupère tous les articles publiés, les trie par date
    de création (plus récent en premier) et les affiche avec pagination
    pour améliorer les performances et l'expérience utilisateur.
    
    Args:
        request (HttpRequest): L'objet requête HTTP de Django
        
    Returns:
        HttpResponse: La page HTML avec la liste des articles
    """
    # Récupération de tous les articles publiés
    # select_related() optimise les requêtes en récupérant aussi auteur et catégorie
    articles_list = Article.objects.filter(
        publie=True
    ).select_related('auteur', 'categorie')
    
    # Configuration de la pagination
    # 5 articles par page pour une navigation facile
    paginator = Paginator(articles_list, 5)
    
    # Récupération du numéro de page depuis l'URL (?page=2)
    page_number = request.GET.get('page')
    
    # Récupération des articles pour la page demandée
    # get_page() gère automatiquement les erreurs (page inexistante, etc.)
    articles = paginator.get_page(page_number)
    
    # Préparation du contexte pour le template
    context = {
        'articles': articles,           # Les articles paginés
        'titre': 'Liste des articles'  # Titre de la page
    }
    
    # Rendu du template avec le contexte
    return render(request, 'blog/liste_articles.html', context)


def detail_article(request, article_id):
    """
    Vue pour afficher le détail d'un article
    
    Cette vue affiche un article complet avec ses métadonnées.
    Elle récupère aussi des articles similaires de la même catégorie
    pour améliorer la navigation de l'utilisateur.
    
    Args:
        request (HttpRequest): L'objet requête HTTP de Django
        article_id (int): L'ID de l'article à afficher
        
    Returns:
        HttpResponse: La page HTML avec le détail de l'article
        
    Raises:
        Http404: Si l'article n'existe pas ou n'est pas publié
    """
    # Récupération de l'article
    # get_object_or_404() lève une erreur 404 si l'article n'existe pas ou n'est pas publié
    article = get_object_or_404(Article, id=article_id, publie=True)
    
    # Recherche d'articles similaires
    articles_similaires = None
    if article.categorie:
        # Si l'article a une catégorie, on cherche d'autres articles de la même catégorie
        articles_similaires = Article.objects.filter(
            categorie=article.categorie,    # Même catégorie
            publie=True                     # Publiés uniquement
        ).exclude(
            id=article.id                   # Exclure l'article actuel
        ).select_related('auteur')[:3]      # Limiter à 3 articles + optimisation requête
    
    # Préparation du contexte pour le template
    context = {
        'article': article,                         # L'article principal
        'articles_similaires': articles_similaires, # Articles de la même catégorie
        'titre': article.titre                      # Titre de la page = titre de l'article
    }
    
    # Rendu du template avec le contexte
    return render(request, 'blog/detail_article.html', context)


def articles_par_categorie(request, categorie_id):
    """
    Vue pour afficher les articles d'une catégorie spécifique
    
    Cette vue filtre les articles par catégorie et les affiche
    dans une page dédiée. Utile pour la navigation thématique.
    
    Args:
        request (HttpRequest): L'objet requête HTTP de Django
        categorie_id (int): L'ID de la catégorie à afficher
        
    Returns:
        HttpResponse: La page HTML avec les articles de la catégorie
        
    Raises:
        Http404: Si la catégorie n'existe pas
    """
    # Récupération de la catégorie
    # get_object_or_404() lève une erreur 404 si la catégorie n'existe pas
    categorie = get_object_or_404(Categorie, id=categorie_id)
    
    # Récupération des articles de cette catégorie
    articles = Article.objects.filter(
        categorie=categorie,        # Articles de cette catégorie uniquement
        publie=True                 # Publiés uniquement
    ).select_related('auteur')      # Optimisation : récupérer aussi l'auteur
    
    # Préparation du contexte pour le template
    context = {
        'articles': articles,                       # Articles de la catégorie
        'categorie': categorie,                     # La catégorie elle-même
        'titre': f'Articles - {categorie.nom}'     # Titre dynamique
    }
    
    # Rendu du template avec le contexte
    return render(request, 'blog/articles_categorie.html', context)
