from django.urls import path
from ..views import article_views

# URLs spécifiques aux articles
urlpatterns = [
    path('articles/', article_views.liste_articles, name='liste_articles'),
    path('article/<int:article_id>/', article_views.detail_article, name='detail_article'),
    path('categorie/<int:categorie_id>/', article_views.articles_par_categorie, name='articles_categorie'),
]
