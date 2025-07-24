"""
Modèle Categorie - Représente une catégorie d'articles

Ce fichier définit le modèle Categorie qui permet de classer
les articles par thématiques. Chaque catégorie a un nom,
une description et une couleur pour l'affichage.
"""

from django.db import models


class Categorie(models.Model):
    """
    Modèle pour les catégories d'articles
    
    Une catégorie permet de regrouper les articles par thème.
    Elle a un nom unique, une description optionnelle et une couleur
    pour l'affichage dans l'interface utilisateur.
    """
    
    # === CHAMP PRINCIPAL ===
    nom = models.CharField(
        max_length=100, 
        unique=True,                    # Chaque catégorie doit avoir un nom unique
        verbose_name="Nom",
        help_text="Le nom de la catégorie (unique, max 100 caractères)"
    )
    
    # === CHAMP DESCRIPTIF ===
    description = models.TextField(
        blank=True,                     # Peut être vide dans les formulaires
        verbose_name="Description",
        help_text="Description optionnelle de la catégorie"
    )
    
    # === CHAMP D'AFFICHAGE ===
    couleur = models.CharField(
        max_length=7,                   # Format hexadécimal : #RRGGBB (7 caractères)
        default="#007bff",              # Couleur bleue par défaut
        verbose_name="Couleur (hex)",
        help_text="Couleur d'affichage au format hexadécimal (ex: #FF0000 pour rouge)"
    )
    
    class Meta:
        """
        Métadonnées du modèle Categorie
        
        Configuration du comportement et de l'affichage
        du modèle dans l'interface d'administration.
        """
        verbose_name = "Catégorie"          # Nom singulier dans l'admin
        verbose_name_plural = "Catégories"  # Nom pluriel dans l'admin
        ordering = ['nom']                  # Tri alphabétique par nom
    
    def __str__(self):
        """
        Représentation textuelle de la catégorie
        
        Utilisée dans l'admin Django et partout où la catégorie
        est convertie en chaîne de caractères.
        
        Returns:
            str: Le nom de la catégorie
        """
        return self.nom
    
    def get_articles_count(self):
        """
        Retourne le nombre d'articles publiés dans cette catégorie
        
        Cette méthode compte uniquement les articles publiés
        (publie=True) pour avoir une statistique pertinente.
        
        Returns:
            int: Le nombre d'articles publiés dans cette catégorie
        """
        # Utilise la relation inverse pour compter les articles
        # article_set est automatiquement créé par Django grâce à la ForeignKey
        return self.article_set.filter(publie=True).count()
    
    def get_latest_articles(self, limit=5):
        """
        Retourne les derniers articles publiés de cette catégorie
        
        Méthode utile pour afficher les articles les plus récents
        d'une catégorie donnée.
        
        Args:
            limit (int): Nombre maximum d'articles à retourner (défaut: 5)
            
        Returns:
            QuerySet: Les derniers articles publiés de cette catégorie
        """
        return self.article_set.filter(
            publie=True
        ).order_by('-date_creation')[:limit]
