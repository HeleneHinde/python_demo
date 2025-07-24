from django.contrib import admin
from ..models import Categorie


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'couleur', 'get_articles_count')
    search_fields = ('nom', 'description')
    list_per_page = 20
    
    def get_articles_count(self, obj):
        """Affiche le nombre d'articles dans l'admin"""
        return obj.get_articles_count()
    
    get_articles_count.short_description = 'Nb articles'
