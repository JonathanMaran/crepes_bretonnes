from django.urls import path, re_path
from . import views

urlpatterns = [
    path('accueil', views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('article/<int:id_article>', views.view_article, name='afficher_article'),
    path('redirection', views.view_redirection, name='redirection'),
    path('date', views.date_actuelle, name='date'),
    path('addition/<int:nombre1>/<int:nombre2>', views.addition, name='addition'),
    # autre manière d'écrire (d4 attend un nombre à 4 chiffres que la vue disposera sous le nom year
    re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.list_articles, name='afficher_liste_articles')
]
