from django import forms
from .models import Article, Category

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
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'status', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input w-full px-4 py-3 border border-gray-300 rounded-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-input w-full px-4 py-3 border border-gray-300 rounded-lg', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-input w-full px-4 py-3 border border-gray-300 rounded-lg'}),
            'icon': forms.TextInput(attrs={'class': 'form-input w-full px-4 py-3 border border-gray-300 rounded-lg'}),
        }
