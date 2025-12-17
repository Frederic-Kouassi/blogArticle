from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    auteur = models.CharField(max_length=100)
    image = models.ImageField(upload_to='articles', blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name