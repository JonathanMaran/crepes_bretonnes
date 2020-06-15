from django.conf.urls import url
from django.urls import path, re_path
from django.views.generic import ListView

from . import views
from .models import Article

urlpatterns = [
    # path('accueil', views.accueil, name='accueil'),
    # Nous allons réécricre l'URL de l'accueil ci dessous
    url(r'^accueil$', views.ListeArticles.as_view(  # model=Article,
        # context_object_name="derniers_articles",    Par souci de lisibilité, nous vous conseillons plutôt de renseigner les classes dans views.py, comme vu précédemment.
        # template_name="blog/accueil.html"
    ), name="blog_liste"),

    # Et nous avons toujours nos autres pages…
    #url(r'^article/(?P<id>\d+)$', views.lire),
    url(r'^categorie/(\w+)$', views.ListeArticles.as_view()),

    #url(r'^(?P<page>\d+)$', views.archives),
    url(r'^categorie/(\d+)$', views.ListeArticles.as_view(), name='blog_categorie'),
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('article/<int:id_article>', views.view_article, name='afficher_article'),
    path('redirection', views.view_redirection, name='redirection'),
    path('contact/', views.contact, name='contact'),
    path('nouveaucontact/', views.nouveau_contact, name='nouveau_contact'),
    path('voircontacts', views.voir_contacts, name='voircontacts'),
    path('date', views.date_actuelle, name='date'),
    path('addition/<int:nombre1>/<int:nombre2>', views.addition, name='addition'),
    # autre manière d'écrire (d4 attend un nombre à 4 chiffres que la vue disposera sous le nom year
    re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.list_articles, name='afficher_liste_articles'),
    url('faq', views.faq, name='faq'),
    url(r'^faq$', views.FAQView.as_view()),  # nous demandons la vue correspondant à la classe FAQView
    # url(r'^faq', TemplateView.as_view(template_name='blog/faq.html')),  POSSIBILITE d'instancier directement TemplateView dans le fichier urls.py en passant l'argument template_name, par conséquent la classe FAQView n'a plus d'intérêt
]
