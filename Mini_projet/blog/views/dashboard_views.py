from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from blog.models import Article, Category, Comment, User

class DashboardBaseView(LoginRequiredMixin, View):
    """
    Base view for dashboard pages to provide common context.
    LoginRequiredMixin ensures only logged-in users access these pages.
    """
    def get_common_context(self, request):
        return {
            "article_count": Article.objects.all().count(), # Total count for sidebar
            "user": request.user,
        }

class UserDashboardView(DashboardBaseView):
    def get(self, request):
        context = self.get_common_context(request)
        
        # Dashboard specific stats
        context.update({
            "total_comments": Comment.objects.count(),
            "new_comments": Comment.objects.filter(status='PENDING').order_by('-created')[:5],
            "published_articles": Article.objects.filter(status='PUBLISHED').order_by('-date')[:5],
            "draft_articles": Article.objects.filter(status='DRAFT').order_by('-date')[:5],
        })
        return render(request, 'dashboard/overview.html', context)

class UserProfileView(DashboardBaseView):
    def get(self, request):
        context = self.get_common_context(request)
        return render(request, 'dashboard/profile.html', context)
        
    def post(self, request):
        current_user = request.user
        
        # Update user fields
        current_user.first_name = request.POST.get("first_name", current_user.first_name)
        current_user.last_name = request.POST.get("last_name", current_user.last_name)
        current_user.email = request.POST.get("email", current_user.email)
        current_user.bio = request.POST.get("bio", current_user.bio)
        current_user.website = request.POST.get("website", current_user.website)
        current_user.location = request.POST.get("location", current_user.location)
        current_user.twitter_username = request.POST.get("twitter_username", current_user.twitter_username)
        current_user.linkedin_url = request.POST.get("linkedin_url", current_user.linkedin_url)
        current_user.github_username = request.POST.get("github_username", current_user.github_username)
        
        if request.FILES.get("avatar"):
            current_user.avatar = request.FILES.get("avatar")
            
        current_user.save()
        messages.success(request, "Profil mis à jour avec succès")
        
        return redirect('user_dashboard') # Or stay on profile: redirect('user_profile')

class UserSettingsView(DashboardBaseView):
    def get(self, request):
        context = self.get_common_context(request)
        return render(request, 'dashboard/settings.html', context)

class UserAnalyticsView(DashboardBaseView):
    def get(self, request):
        context = self.get_common_context(request)
        
        # Analytics logic (e.g., top articles)
        top_articles = Article.objects.filter(status='PUBLISHED').order_by('-date')[:3] # Using date as proxy for popularity for now
        
        context.update({
             "top_articles": top_articles
        })
        return render(request, 'dashboard/analytics.html', context)

class CreateBlogView(DashboardBaseView):
    def get(self, request):
        context = self.get_common_context(request)
        context["categories"] = Category.objects.all()
        return render(request, 'dashboard/create_blog.html', context)
        
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
        current_user = request.user

        if name and description and category_id:
            category = get_object_or_404(Category, id=category_id)
            Article.objects.create(
                name=name,
                description=description,
                author=current_user,
                category=category,
                image=image,
                status=status,
                tags=tags,
                featured=featured,
                allow_comments=allow_comments,
                newsletter_feature=newsletter_feature,
            )
            messages.success(request, "Article créé avec succès")
            return redirect('user_dashboard')

        messages.error(request, "Erreur lors de la création de l'article")
        return redirect('create_blog')
