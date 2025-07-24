"""
Configuration de l'interface d'administration pour les Articles

Ce fichier personnalise l'interface d'administration Django
pour le modèle Article. Il définit comment les articles
sont affichés, filtrés et édités dans l'admin.
"""

from django.contrib import admin
from django.utils.html import format_html
from ..models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Configuration de l'administration pour le modèle Article
    
    Cette classe personnalise l'interface d'administration Django
    pour offrir une meilleure expérience de gestion des articles.
    """
    
    # === AFFICHAGE DE LA LISTE ===
    list_display = (
        'titre',                    # Titre de l'article
        'auteur',                   # Auteur de l'article
        'categorie',                # Catégorie de l'article
        'publie',                   # Statut de publication
        'is_recent_display',        # Indicateur "récent" (méthode personnalisée)
        'date_creation'             # Date de création
    )
    
    # === FILTRES LATÉRAUX ===
    list_filter = (
        'publie',                   # Filtre par statut de publication
        'categorie',                # Filtre par catégorie
        'date_creation',            # Filtre par date de création
        'auteur'                    # Filtre par auteur
    )
    
    # === CHAMPS DE RECHERCHE ===
    search_fields = (
        'titre',                    # Recherche dans le titre
        'contenu'                   # Recherche dans le contenu
    )
    
    # === ÉDITION RAPIDE ===
    list_editable = ('publie',)    # Permet de modifier le statut directement dans la liste
    
    # === NAVIGATION PAR DATE ===
    date_hierarchy = 'date_creation'  # Ajoute une navigation par date en haut
    
    # === PAGINATION ===
    list_per_page = 20              # Nombre d'articles par page
    
    # === CHAMPS EN LECTURE SEULE ===
    readonly_fields = ('date_creation', 'date_modification')
    
    # === ORGANISATION DES CHAMPS DANS LE FORMULAIRE ===
    fieldsets = (
        # Premier groupe : Contenu principal
        ('Contenu', {
            'fields': ('titre', 'contenu', 'categorie'),
            'description': 'Informations principales de l\'article'
        }),
        
        # Deuxième groupe : Publication
        ('Publication', {
            'fields': ('auteur', 'publie'),
            'description': 'Paramètres de publication'
        }),
        
        # Troisième groupe : Dates (repliable)
        ('Dates', {
            'fields': ('date_creation', 'date_modification'),
            'classes': ('collapse',),    # Groupe repliable par défaut
            'description': 'Informations de création et modification'
        }),
    )
    
    def is_recent_display(self, obj):
        """
        Affiche si l'article est récent avec une icône colorée
        
        Cette méthode personnalisée ajoute une colonne dans la liste
        des articles pour indiquer visuellement si l'article est récent.
        
        Args:
            obj (Article): L'instance d'article à évaluer
            
        Returns:
            str: HTML formaté avec icône et couleur
        """
        if obj.is_recent():
            # Article récent : icône verte avec texte
            return format_html(
                '<span style="color: green; font-weight: bold;">✓ Récent</span>'
            )
        else:
            # Article ancien : icône grise
            return format_html(
                '<span style="color: gray;">⏰ Ancien</span>'
            )
    
    # Configuration de la colonne personnalisée
    is_recent_display.short_description = 'Récent'  # Titre de la colonne
    is_recent_display.admin_order_field = 'date_creation'  # Permet le tri par cette colonne
    
    def save_model(self, request, obj, form, change):
        """
        Personnalise la sauvegarde d'un article
        
        Cette méthode est appelée quand un article est sauvegardé
        depuis l'interface d'administration. Elle permet d'ajouter
        une logique personnalisée.
        
        Args:
            request (HttpRequest): La requête HTTP
            obj (Article): L'instance d'article à sauvegarder
            form (ModelForm): Le formulaire soumis
            change (bool): True si c'est une modification, False si c'est une création
        """
        # Si c'est un nouvel article (pas une modification)
        if not change:
            # Définit automatiquement l'auteur comme l'utilisateur connecté
            obj.auteur = request.user
        
        # Appelle la méthode de sauvegarde standard
        super().save_model(request, obj, form, change)
    
    def get_queryset(self, request):
        """
        Optimise les requêtes pour la liste des articles
        
        Cette méthode optimise les requêtes de base de données
        en récupérant les relations en une seule requête.
        
        Args:
            request (HttpRequest): La requête HTTP
            
        Returns:
            QuerySet: Les articles avec optimisations
        """
        # Utilise select_related pour récupérer auteur et catégorie
        # en une seule requête au lieu de requêtes séparées
        return super().get_queryset(request).select_related('auteur', 'categorie')
