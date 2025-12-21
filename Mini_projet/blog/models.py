from django.db import models

# Create your models here.

from django.db import models


    
    
    
class Utilisateurs (models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"




class Article(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    auteur = models.ForeignKey( Utilisateurs,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles', blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name