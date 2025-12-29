from django.urls import path
from blog.views import HomeView, about,DeleteArticle,  contact, Admin_dashboaord,DeleteCategory,  User_dashboaord, RegisterView, LoginView, VerifyEmailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("admin-dashboard/",Admin_dashboaord.as_view(), name="admin_dashboard"),
    path("user-dashboard/", User_dashboaord.as_view(), name="user_dashboard"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("verify-email/", VerifyEmailView.as_view(), name="verify_email"),
    path("category/delete/<uuid:id>/", DeleteCategory.as_view(), name="delete_category"),
    path("article/delete/<uuid:id>/",DeleteArticle.as_view(), name="delete_article")

  
]
