from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'description', 'author', 'image']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Titre de l’article'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Description',
                'rows': 5
            }),
            'author': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Nom de l’auteur'
            }),
        }
