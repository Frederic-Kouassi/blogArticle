from django.shortcuts import render,redirect, get_object_or_404
from blog.models import *
from django.utils.text import slugify
from blog.forms import ArticleForm
from django.views import View



# Create your views here.

class HomeView(View):
     def get(self, request):
        categories = Category.objects.all()
        articles = Article.objects.all()
        return render(request, 'home.html', {"categorie": categories, "articles":articles})
        

class ArticleDetailView(View):
    def get(self, request, slug):
        categories = Category.objects.all()
        article = get_object_or_404(Article, slug=slug)

        return render(request, 'page_detail.html', {
            'categorie': categories,
            'article': article
        })

class Admin_dashboaord(View):

    def get(self, request):
        categories = Category.objects.all()
        articles = Article.objects.all()
        return render(
            request,
            'admin_dashboard.html',
            {"categorie": categories, "articles":articles}
        )

    def post(self, request):
        data= request.POST
        name =data.get("name")
        description = data.get("description")
        status = data.get("status")

        if name:
            Category.objects.create(
                name=name,
                slug=slugify(name),
                description=description,
                status=status
            )

        return redirect("admin_dashboard")
  
        return redirect("admin_dashboard")

    
class DeleteCategory(View):
    def post(self, request, id):
        category = get_object_or_404(Category, id=id)
        category.delete()
        return redirect("admin_dashboard")
  

class EditCategory(View):

    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        return render(request, "editcategory.html", {"category": category})

    def post(self, request, id):
        category = get_object_or_404(Category, id=id)

        category.name = request.POST.get("name")
        category.description = request.POST.get("description")
        category.status = request.POST.get("status")
        category.slug = slugify(category.name)

        category.save()
        return redirect("admin_dashboard")  

    
  
  


class User_dashboaord(View):
    def get(self, request):
       articles = Article.objects.all()
       categories = Category.objects.all()
       user = User.objects.all()
       return render(request, 'user_dashboard.html', {"categorie": categories, "user": user,"articles":articles})
    
    def post(self, request):
        data= request.POST
        name = data.get("name")
        description = data.get("description")
        category_id = data.get("category")
        status = data.get("status")
        tags = data.get("tags")

        featured = "featured" in request.POST
        allow_comments = "allow_comments" in request.POST
        newsletter_feature = "newsletter_feature" in request.POST

        image = request.FILES.get("image")

        if name and description and category_id:
            
            category = get_object_or_404(Category, id=category_id)
            author = request.user 

            Article.objects.create(
                name=name,
                description=description,
                author=author,
                category=category,
                image=image,
                status=status,
                tags=tags,
                featured=featured,
                allow_comments=allow_comments,
                newsletter_feature=newsletter_feature,
            )

            return redirect("user_dashboard")
        return redirect("user_dashboard")
        
    
class DeleteArticle(View):
    def post(self, request, id):
        article = get_object_or_404(
            Article,
            id=id,
            author=request.user
        )
        article.delete()
        return redirect("user_dashboard")





class EditArticle(View):

    def get(self, request, id):
        article = get_object_or_404(
            Article,
            id=id,
            author=request.user
        )
        categories = Category.objects.all()

        return render(
            request,
            "edit_article.html",
            {
                "article": article,
                "categories": categories
            }
        )

    def post(self, request, id):
        article = get_object_or_404(
            Article,
            id=id,
            author=request.user
        )

        article.name = request.POST.get("name")
        article.description = request.POST.get("description")
        article.category_id = request.POST.get("category")
        article.status = request.POST.get("status")
        article.tags = request.POST.get("tags")

        article.featured = "featured" in request.POST
        article.newsletter_feature = "newsletter_feature" in request.POST
        article.allow_comments = "allow_comments" in request.POST

        if request.FILES.get("image"):
            article.image = request.FILES.get("image")

        article.save()
        return redirect("user_dashboard")


def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')


    


