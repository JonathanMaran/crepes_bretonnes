from django.shortcuts import render, redirect, get_object_or_404
from mini_url.models import MiniURL
from mini_url.forms import MiniURLForm


# Create your views here.

def liste(request):
    """
    afficher les redirections
    """
    minis = MiniURL.objects.order_by('-nombre_acces')

    return render(request, 'liste.html', locals())


def nouveau(request):
    """
    ajout d'une redirection
    """
    if request.method == "POST":
        form = MiniURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(liste)  # si le formulaire est valide, il faut renvoyer à l'affichage des redirections

    else:
        form = MiniURLForm()

    return render(request, 'nouveau.html', {'form': form})


def redirection(request, code):
    """Redirection vers l'URL enregistrée"""
    mini = get_object_or_404(MiniURL, code=code)
    mini.nombre_acces += 1
    mini.save()

    return redirect(mini.url, permanent=True)
