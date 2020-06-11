from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactForm, NouveauContactForm
from blog.models import Article, Contact


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


# Formulaire

def contact(request):
    """
    Construire le formulaire soit avec les données postées, soit vide si l'utilisateur accède pour la première fois à la page
    """
    form = ContactForm(request.POST or None)
    """
    Nous vérifions que les données envoyées sont valides. Cette méthode renvoie false s'il n'y a pas de données dans le formulaire ou qu'il contient des erreurs.
    """
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e mail grâce aux données que nous venons de récupérer
        envoi = True

    # On affiche la page du formulaire quoiqu'il arrive
    return render(request, 'blog/contact.html', locals())


def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None,
                              request.FILES)  # request.POST => pour els donnés textuelles et request.FILES pour les fichiers comme les photos
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'blog/nouveaucontact.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })


def voir_contacts(request):
    return render(
        request,
        'blog/voir_contacts.html',
        {'contacts': Contact.objects.all()}
    )
