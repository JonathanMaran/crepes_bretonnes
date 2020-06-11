from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Article


# Create your views here.
# contiendra toutes les vues de l'application


def accueil(request):
    # Afficher tous les articles de notre blog
    articles = Article.objects.all()  # Nous récupérons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})
    # HttpResponse permet de retourner une réponse texte brut ou html


def lire(request, id, slug):
    """
    afficher un article complet
    """
    article = get_object_or_404(Article, id=id, slug=slug)

    return render(request, 'blog/lire.html', {'article': article})


def view_redirection(request):
    return HttpResponse("Vous avez été redirigé")


def view_article(request, id_article):
    """
      Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
      Son ID est le second paramètre de la fonction (pour rappel, le premier
      paramètre est TOUJOURS la requête de l'utilisateur)
      """
    # permet de lever une erreur 404 si id article sup à 100
    if id_article > 100:
        return redirect(view_redirection)
    else:
        return HttpResponse("Vous avez demandé l'article n°{} !".format(id_article))


def list_articles(request, year, month):
    """
    liste des articles d'un mois précis
    """
    return HttpResponse("Vous avez demandé les articles de {} {}".format(year, month))


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    # retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())
