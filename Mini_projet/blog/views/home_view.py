import logging
from django.contrib import messages
from blog.forms import ArticleForm, CategoryForm
from django.views import View
from blog.models import Article, Category, User, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.core.paginator import Paginator

logger = logging.getLogger(__name__)


# Create your views here.

class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        articles = Article.objects.filter(status='PUBLISHED').order_by('-date')
        return render(request, 'home.html', {
            "categories": categories,
            "articles": articles
        })
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
        # Stats logic for new dashboard
        users_count = User.objects.count()
        articles_count = Article.objects.count()
        comments_count = Comment.objects.count()
        categories = Category.objects.all()
        articles = Article.objects.order_by('-date')[:5]
 # Recent articles

        return render(
            request,
            'admin_dashboard.html',
            {
                "users_count": users_count,
                "articles_count": articles_count,
                "comments_count": comments_count,
                "categories": categories,
                "articles": articles,
                "active_tab": "dashboard"
            }
        )

    

class AdminCategoryView(View):
    def get(self, request):
        if not request.user.is_authenticated or not request.user.is_staff:
            return redirect('login')
        
        categories = Category.objects.all().order_by('-id')
        return render(request, "admin_categories.html", {
            "categories": categories,
            "active_tab": "categories"
        })

    def post(self, request):
        if not request.user.is_authenticated or not request.user.is_staff:
            return redirect('login')
            
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                category = form.save(commit=False)
                category.slug = slugify(category.name)
                category.save()
                messages.success(request, "Category created successfully")
            except Exception as e:
                logger.error(f"Error creating category: {e}")
                messages.error(request, f"Error creating category: {e}")
        else:
            logger.error(f"Category form validation error: {form.errors}")
            messages.error(request, "Error creating category. Check form data.")
            
        return redirect("admin_categories")

class DeleteCategory(View):
    def post(self, request, id):
        try:
            category = get_object_or_404(Category, id=id)
            category.delete()
            messages.success(request, "Category deleted successfully")
        except Exception as e:
            logger.error(f"Error deleting category {id}: {e}")
            messages.error(request, f"Error deleting category: {e}")
        return redirect("admin_categories")
  

class EditCategory(View):

    def post(self, request, id):
        try:
            category = get_object_or_404(Category, id=id)
            
            # We can use the form to update as well
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                cat = form.save(commit=False)
                cat.slug = slugify(cat.name)
                cat.save()
                messages.success(request, "Category updated successfully")
            else:
                logger.warning(f"Category update form invalid, trying manual fallback. Errors: {form.errors}")
                 # Fallback manual update if form validation fails strangely or for partial updates
                category.name = request.POST.get("name")
                category.description = request.POST.get("description")
                category.status = request.POST.get("status")
                if request.POST.get("icon"):
                    category.icon = request.POST.get("icon")
                category.slug = slugify(category.name)
                category.save()
                messages.success(request, "Category updated successfully")
        except Exception as e:
            logger.error(f"Error updating category {id}: {e}")
            messages.error(request, f"Error updating category: {e}")

        return redirect("admin_categories")  

    
  


class User_dashboaord(View):
   
    def get(self, request):
        article_list = Article.objects.all().order_by('-date')
        categories = Category.objects.all()
        users = User.objects.all()

        paginator = Paginator(article_list, 2)  # 5 articles par page
        page_number = request.GET.get('page')
        articles = paginator.get_page(page_number)

        return render(request, 'user_dashboard.html', {
            "categorie": categories,
            "article_count": article_list.count(),
            "user": users,
            "articles": articles
        })
        
        
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
        article = get_object_or_404(Article, id=id, author=request.user)
        try:
            article.delete()
            messages.success(request, "Article deleted successfully")
        except Exception as e:
            logger.error(f"Error deleting article {id}: {e}")
            messages.error(request, "Error deleting article")
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
        try:
            article = get_object_or_404(
                Article,
                id=id,
                author=request.user  
            )

            # Update via ModelForm
            form = ArticleForm(request.POST, request.FILES, instance=article)

            if form.is_valid():
                art = form.save(commit=False)
                art.slug = slugify(art.name)
                art.save()
                messages.success(request, "Article updated successfully")
            else:
                logger.warning(
                    f"Article update form invalid, fallback used. Errors: {form.errors}"
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

                article.slug = slugify(article.name)
                article.save()

                messages.success(request, "Article updated successfully")

        except Exception as e:
            logger.error(f"Error updating article {id}: {e}")
            messages.error(request, f"Error updating article: {e}")

        return redirect("user_dashboard")
        

def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')


def blog(request):
    article_list = Article.objects.all().order_by('-date')
    categories = Category.objects.all()
    users = User.objects.all()

    paginator = Paginator(article_list, 2)  # 5 articles par page
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    # Récupérer l'onglet actif depuis l'URL ou défaut
    active_tab = request.GET.get('tab', 'my-blogs')

    return render(request, 'blog.html', {
        "categorie": categories,
        "article_count": article_list.count(),
        "user": users,
        "articles": articles,
        "active_tab": active_tab
    })
    
    


    


