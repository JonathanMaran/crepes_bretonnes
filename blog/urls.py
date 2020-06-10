from django.urls import path, re_path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('article/<int:id_article>', views.view_article),
    # autre manière d'écrire (d4 attend un nombre à 4 chiffres que la vue disposera sous le nom year
    re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.list_articles)
]
