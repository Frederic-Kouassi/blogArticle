from django.shortcuts import render,redirect, get_object_or_404
from .models import Article,Utilisateurs
from .forms import ArticleForm

# Create your views here.

from django.shortcuts import render, redirect
from .models import Article, Utilisateurs


def index(request):
    users = Utilisateurs.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        auteur = request.POST.get("auteur")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        Article.objects.create(
            name=name,
            auteur_id=auteur,
            description=description,
            image=image
        )

        return redirect("articles")

    return render(request, "blog/index.html", {
        "users": users
    })




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
        article.auteur = request.POST.get('auteur')
        article.description = request.POST.get('description')

       
        if request.FILES.get('image'):
            article.image = request.FILES.get('image')

        article.save()
        return redirect('articles')

    return render(
        request,
        'blog/updateArticle.html',
        {'article': article}
    )


def create_users(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        email = request.POST.get("email")
        telephone = request.POST.get("telephone")
        adresse = request.POST.get("adresse")

        Utilisateurs.objects.create(
            nom=nom,
            prenom=prenom,
            email=email,
            telephone=telephone,
            adresse=adresse
        )
        return redirect("articles")



    return render(request, "blog/create_User.html")





def liste_user(request):
    users = Utilisateurs.objects.all()
    return render(request, "blog/user.html", {
        "users": users
    })







def connexion(request):
    error = None

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Utilisateurs.objects.get(email=email)

            if user.check_password(password):
              
                request.session["user_id"] = user.id
                request.session["user_name"] = f"{user.prenom} {user.nom}"
                return redirect("articles")
            else:
                error = "Mot de passe incorrect"

        except Utilisateurs.DoesNotExist:
            error = "Utilisateur introuvable"

    return render(request, "blog/connexion.html")


def logout_view(request):
    request.session.flush()
    return redirect("login")
