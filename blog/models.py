from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
# un modèle s'écrit sous la forme d'une classe et représente une table dans la base de données, dont les attributs correspondent aux champs de la table
from django.utils import timezone


class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Date de parution")
    # CASCADE signifie qu'en cas de suppresion de la catégorie, tous les articles ayant cette catégorie seront également supprimés
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']

    # la méthode __str__ permet d'afficher le titre de l'article dans
    def __str__(self):
        """
        Cette méthode que nosu définirons dans tous les modèles nous permettra de reconnaître facilement les différents
        objets que nosu traiterons plus tard dans l'administration
        :return:
        """

        return self.titre


class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


# -------------------------------------
# Second exemple de class/tables OneToOneField

class Moteur(models.Model):
    nom = models.CharField(max_length=25)

    def __str__(self):
        return self.nom


class Voiture(models.Model):
    nom = models.CharField(max_length=25)
    moteur = models.OneToOneField(Moteur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


# -------------------------------------
# Troisième exemple de class/tables ManytoManyField

class Produit(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Vendeur(models.Model):
    nom = models.CharField(max_length=30)
    # related name ='+' désactive la relation inverse
    produits = models.ManyToManyField(Produit, through='Offre', related_name='+')
    produits_sans_prix = models.ManyToManyField(Produit, related_name="vendeurs")

    def __str__(self):
        return self.nom


class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    vendeur = models.ForeignKey(Vendeur, on_delete=models.CASCADE)

    def __str__(self):
        return "{} vendu par {}".format(self.produit, self.vendeur)


# -----------------------------------------------------------------------------

def renommage(instance, nom_fichier):
    return "{}-{}".format(instance.id, nom_fichier)


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.nom


class Document(models.Model):
    nom = models.CharField(max_length=100)
    doc = models.FileField(upload_to=renommage, verbose_name="Document")


# Chapitre sur les requêtes complexes avec Q

class Eleve(models.Model):
    nom = models.CharField(max_length=31)
    moyenne = models.IntegerField(default=10)
    commentaires = GenericRelation('Commentaire')
    # relation générique en sens inverse


    def __str__(self):
        return "Eleve {0} ({1}/20 de moyenne)".format(self.nom, self.moyenne)


class Commentaire(models.Model):
    auteur = models.CharField(max_length=255)
    contenu = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "Commentaire de {0} sur {1}".format(self.auteur, self.content_object)
