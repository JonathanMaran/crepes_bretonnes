from django.db import models

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null = True)
    date = models.DateTimeField(verbose_name= "Date de parution")

