from django.shortcuts import render,redirect, get_object_or_404
from blog.models import *
from django.utils.text import slugify
from blog.forms import ArticleForm
from django.views import View



# Create your views here.

class HomeView(View):
     def get(self, request):
        return render(request, 'home.html')
        


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
        name = request.POST.get("name")
        description = request.POST.get("description")
        status = request.POST.get("status")

        if name:
            Category.objects.create(
                name=name,
                slug=slugify(name),
                description=description,
                status=status
            )

        return redirect("admin_dashboard")
    
class DeleteCategory(View):
    def post(self, request, id):
        category = get_object_or_404(Category, id=id)
        category.delete()
        return redirect("admin_dashboard")
    
  
    def edit(self, request, id):
        category = get_object_or_404(Category, id=id)
        return render(request, "edit_category.html", {"category": category})
    
    
    def update(self, request, id):
        category = get_object_or_404(Category, id=id)

        name = request.POST.get("name")
        description = request.POST.get("description")
        status = request.POST.get("status")

        if name:
            category.name = name
            category.slug = slugify(name)
            category.description = description
            category.status = status
            category.save()

        return redirect("admin_dashboard")



class User_dashboaord(View):
    def get(self, request):
       articles = Article.objects.all()
       categories = Category.objects.all()
       user = User.objects.all()
       return render(request, 'user_dashboard.html', {"categorie": categories, "user": user,"articles":articles})
    
    def post(self, request):
        name = request.POST.get("name")
        description = request.POST.get("description")
        category_id = request.POST.get("category")
        status = request.POST.get("status")
        tags = request.POST.get("tags")

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





def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')


    


