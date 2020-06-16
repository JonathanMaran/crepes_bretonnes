# nous devons nécessairement créer un fichier __init__ vide, sans quoi Django ne pourra rien faire.
from random import randint

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

"""
#Pour intégrer des tags et filtres dans n'importe quel template =>
{% load blog_extras %}

Filtre upper sur la variable "texte" :
{{ texte|upper }}            

Filtre truncatewords, avec comme argument "80" sur la variable "texte" :
{{ texte|truncatewords:80 }}
"""


# création du premier filtre
@register.filter(is_safe=True)  # echapper les caractères spéciaux
def citation(texte):
    """
    Affiche le texte passé en paramètre, encadré de guillemets
    français doubles et d'espaces insécables.
    """
    res = "&laquo; {} &raquo;".format(escape(texte))
    return mark_safe(res)


@register.filter
def smart_truncate(texte, nb_caracteres=30):
    # Nous vérifions tout d'abord que l'argument passé est bien un nombre

    try:
        nb_caracteres = int(nb_caracteres)
    except:
        return texte

    # Si la chaîne est plus petite que le nombre de caractères maximum voulus, nous renvoyons directement la chaîne telle quelle.
    if len(texte) <= nb_caracteres:
        return texte

    # Sinon, nous coupons au maximum, tout en gardant le caractère suivant pour savoir si nous avons coupé à la fin d'un mot ou en plein milieu

    texte = texte[:nb_caracteres + 1]

    # nous vérifions d'abord que le dernier caractère n'est pas un espace, autrement, il est inutile d'enlever le dernier mot !

    if texte[-1:] != ' ':
        mots = texte.split(' ')[:-1]
        texte = ' '.join(mots)
    else:
        texte = texte[0:-1]

    return texte + '...'


@register.tag()
def random(parser, token):
    """Tag générant un nombre aléatoire, entre les bornes données en arguments"""
    # Séparation des paramètres contenus dans l'object token. Le premier
    # élément du token est toujours le nom du tag en cours
    try:
        nom_tag, begin, end = token.split_contents()
    except ValueError:
        msg = 'Le tag %s doit prendre exactement deux arguments.' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)

    # Nous vérifions ensuite que nos deux paramètres sont bien des entiers
    try:
        begin, end = int(begin), int(end)
    except ValueError:
        msg = 'Les arguments du tag %s sont obligatoirement des entiers.' % nom_tag
        raise template.TemplateSyntaxError(msg)

    # Nous vérifions si le premier est inférieur au second
    if begin > end:
        msg = 'L\'argument "begin" doit obligatoirement être inférieur à l\'argument "end" dans le taf %s.' % nom_tag
        raise template.TemplateSyntaxError(msg)

    return RandomNode(begin, end)


class RandomNode(template.Node):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def render(self, context):
        return str(randint(self.begin, self.end))
