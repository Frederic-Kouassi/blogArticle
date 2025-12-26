from django.shortcuts import render,redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def user_dashboard(request):
    return render(request, 'user_dashboard.html')


def index(request):
    if request.method == "POST":
        name=request.POST.get("name"),
        author=request.POST.get("author"),
        description=request.POST.get("description"),
        image=request.FILES.get("image")
        Article.objects.create(name=name, author=author, description=description,image=image)
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

    


def modifier_article(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        article.name = request.POST.get('name')
        article.author = request.POST.get('author')
        article.description = request.POST.get('description')

        # Image facultative
        if request.FILES.get('image'):
            article.image = request.FILES.get('image')

        article.save()
        return redirect('articles')

    return render(
        request,
        'blog/updateArticle.html',
        {'article': article}
    )
