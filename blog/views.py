from django.http import HttpResponse, Http404
from django.shortcuts import render


# Create your views here.
# contiendra toutes les vues de l'application
def home(request):
    # exemple de page non valide au niveau HTML pour que l'exemple soit concis
    return HttpResponse("<h1>Bienvenue sur mon blog</h1>"
                        "<p>Les crêpes bretonnes ça tue des mouettes en plein vol !")
    # HttpResponse permet de retourner une réponse texte brut ou html


def view_article(request, id_article):
    """
      Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
      Son ID est le second paramètre de la fonction (pour rappel, le premier
      paramètre est TOUJOURS la requête de l'utilisateur)
      """
    # permet de lever une erreur 404 si id article sup à 100
    if id_article > 100:
        raise Http404

    return HttpResponse("Vous avez demandé l'article n°{} !".format(id_article))


def list_articles(request, year, month):
    """
    liste des articles d'un mois précis
    """
    return HttpResponse("Vous avez demandé les articles de {} {}".format(year, month))
