from django.shortcuts import render,redirect, get_object_or_404
from blog.models import Article
from blog.forms import ArticleForm

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
