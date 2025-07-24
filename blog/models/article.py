"""
Modèle Article - Représente un article de blog

Ce fichier définit le modèle Article qui gère les articles du blog.
Il inclut toutes les informations nécessaires pour un article :
- Contenu (titre, texte)
- Métadonnées (auteur, catégorie, dates)
- État de publication
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Article(models.Model):
    """
    Modèle pour les articles de blog
    
    Ce modèle représente un article de blog avec toutes ses propriétés.
    Il hérite de models.Model qui fournit les fonctionnalités de base
    pour interagir avec la base de données.
    """
    
    # === CHAMPS DE CONTENU ===
    titre = models.CharField(
        max_length=200, 
        verbose_name="Titre",
        help_text="Le titre de l'article (maximum 200 caractères)"
    )
    
    contenu = models.TextField(
        verbose_name="Contenu",
        help_text="Le contenu principal de l'article (texte long)"
    )
    
    # === CHAMPS DE RELATIONS ===
    auteur = models.ForeignKey(
        User,                           # Référence vers le modèle User de Django
        on_delete=models.SET_NULL,      # Si l'utilisateur est supprimé, l'article reste mais auteur devient NULL
        null=True,                      # Permet la valeur NULL en base de données
        blank=True,                     # Permet le champ vide dans les formulaires
        verbose_name="Auteur",
        help_text="L'auteur de cet article"
    )
    
    categorie = models.ForeignKey(
        'Categorie',                    # Référence vers le modèle Categorie (en string car défini ailleurs)
        on_delete=models.SET_NULL,      # Si la catégorie est supprimée, l'article reste
        null=True,                      # Champ optionnel
        blank=True,                     # Peut être vide dans les formulaires
        verbose_name="Catégorie",
        help_text="La catégorie de cet article (optionnel)"
    )
    
    # === CHAMPS DE DATES ===
    date_creation = models.DateTimeField(
        default=timezone.now,           # Date/heure automatique à la création
        verbose_name="Date de création",
        help_text="Date et heure de création de l'article"
    )
    
    date_modification = models.DateTimeField(
        auto_now=True,                  # Mise à jour automatique à chaque sauvegarde
        verbose_name="Date de modification",
        help_text="Date et heure de la dernière modification"
    )
    
    # === CHAMPS DE STATUT ===
    publie = models.BooleanField(
        default=False,                  # Par défaut, les articles ne sont pas publiés
        verbose_name="Publié",
        help_text="Cochez pour rendre l'article visible sur le site"
    )
    
    class Meta:
        """
        Métadonnées du modèle Article
        
        Cette classe interne définit les options de configuration
        pour le modèle Article.
        """
        verbose_name = "Article"                    # Nom singulier dans l'interface admin
        verbose_name_plural = "Articles"            # Nom pluriel dans l'interface admin
        ordering = ['-date_creation']               # Tri par défaut : plus récent en premier
        
        # Autres options possibles :
        # db_table = 'blog_article'               # Nom personnalisé de la table
        # unique_together = ['titre', 'auteur']   # Contrainte d'unicité
    
    def __str__(self):
        """
        Représentation textuelle de l'objet
        
        Cette méthode définit comment l'objet Article est affiché
        dans l'admin Django et lors des conversions en string.
        
        Returns:
            str: Le titre de l'article
        """
        return self.titre
    
    def get_absolute_url(self):
        """
        Retourne l'URL absolue de l'article
        
        Cette méthode est utilisée par Django pour générer
        automatiquement les liens vers cet article.
        
        Returns:
            str: L'URL complète vers la page de détail de cet article
        """
        return reverse('detail_article', args=[str(self.id)])
    
    def get_resume(self, nb_mots=30):
        """
        Retourne un résumé de l'article
        
        Cette méthode crée un extrait du contenu de l'article
        en limitant le nombre de mots.
        
        Args:
            nb_mots (int): Nombre maximum de mots dans le résumé (défaut: 30)
            
        Returns:
            str: Le résumé de l'article avec "..." si tronqué
        """
        mots = self.contenu.split()                 # Sépare le contenu en mots
        if len(mots) > nb_mots:                     # Si plus de mots que la limite
            return ' '.join(mots[:nb_mots]) + '...' # Retourne les premiers mots + "..."
        return self.contenu                         # Sinon retourne tout le contenu
    
    def is_recent(self):
        """
        Vérifie si l'article a été créé récemment
        
        Un article est considéré comme récent s'il a été créé
        il y a moins de 7 jours.
        
        Returns:
            bool: True si l'article est récent, False sinon
        """
        from datetime import timedelta
        # Compare la date de création avec la date actuelle moins 7 jours
        return self.date_creation >= timezone.now() - timedelta(days=7)
