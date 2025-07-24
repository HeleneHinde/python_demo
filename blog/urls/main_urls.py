from django.urls import path, include
from ..views import home_views, article_views

# URLs principales de l'application blog
urlpatterns = [
    # Pages d'accueil
    path('', home_views.accueil, name='accueil'),
    path('about/', home_views.about, name='about'),
    
    # URLs des articles
    path('', include('blog.urls.article_urls')),
]
