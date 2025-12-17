from django.shortcuts import render,redirect, get_object_or_404
from .models import Article

# Create your views here.

def index(request):
    if request.method == "POST":
        name=request.POST.get("name"),
        auteur=request.POST.get("auteur"),
        description=request.POST.get("description"),
        image=request.FILES.get("image")
        Article.objects.create(name=name, auteur=auteur, description=description,image=image)
        return redirect('articles')
    return render (request, 'blog/index.html')



def liste_article(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, "blog/affiche.html", {
        "articles": articles
    })
    

def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "blog/detail.html", {"article": article})


def supprimer(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect("articles")  

    