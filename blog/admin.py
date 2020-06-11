from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.text import Truncator

from blog.models import Categorie, Article


# Register your models here.
# va permettre de définir ce que vous souhaitez afficher et modifier comme modèles depuis l'administration de l'application générée automatiquement

class ArticleAdmin(admin.ModelAdmin):
    # Liste des champs du modèle à afficher dans le tableau
    list_display = ('titre', 'auteur', 'date', 'apercu_contenu', 'slug')
    # Liste des champs à parti desquels nous pourrons filtrer les entrées
    list_filter = ('auteur', 'categorie')
    # Permet de filtrer par date de façon intuitive
    date_hierarchy = 'date'
    # Tri par défaut du tableau
    ordering = ('date',)
    # Configuration du champ de recherche
    search_fields = ('titre', 'contenu')
    # Prend une liste des champs qui seront affichés dans l'ordre souhaité (cela peut permettre de cacher des champs et de changer leur ordre)
    # fields = ('titre', 'auteur', 'categorie', 'contenu') => remplacé par le fieldsets si dessous
    fieldsets = (
        #Fieldset 1: meta info (titre, auteur...)
        ('Général', {
            'classes': ['collapse',], # le collapse cache cette partie, qui peut être affichée par la suite (classe css)
            'fields': ('titre', 'slug', 'auteur', 'categorie') # liste des champs à afficher dans le fieldset
        }),
        #Fieldset 2: contenu de l'article
        ('Contenu de l\'article', {
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !', # description qui sera affichée en haut du fiedset, avant le premier champ
            'fields': ('contenu', )
        }),

    )
    # remplir les champs de type SlugField
    prepopulated_fields = {'slug': ('titre', )}

    # Colonne personnalisées
    def apercu_contenu(self, article):
        """
        retourne les 40 premiers caractères du contenu de l'article, suivi de points de suspension si le texte est plus long.

        """
        return Truncator(article.contenu).chars(40, truncate='...')

    #En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'


admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
