from django.urls import path
from blog.views import HomeView, blog, about,ArticleDetailView,Comments,CommentLikeView, user_logout, DeleteComment ,DeleteArticle,EditArticle, EditCategory, contact, Admin_dashboaord, AdminCategoryView, DeleteCategory,  User_dashboaord, RegisterView, LoginView, VerifyEmailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("about/", about, name="about"),
     path("blog/", blog, name="blog"),
    path("contact/", contact, name="contact"),
    path('logout/', user_logout, name='logout'),
    
    path("admin-dashboard/",Admin_dashboaord.as_view(), name="admin_dashboard"),
    path("admin-dashboard/categories/", AdminCategoryView.as_view(), name="admin_categories"),
    path("user-dashboard/", User_dashboaord.as_view(), name="user_dashboard"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("verify-email/", VerifyEmailView.as_view(), name="verify_email"),
    path("category/delete/<uuid:id>/", DeleteCategory.as_view(), name="delete_category"),
    path("article/delete/<uuid:id>/",DeleteArticle.as_view(), name="delete_article"),
    path("category/edit/<uuid:id>/", EditCategory.as_view(), name="edit_category"),
    path("article/edit/<uuid:id>/", EditArticle.as_view(), name="edit_article"),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('comments', Comments.as_view(), name='comments'),
    path('comments/<uuid:comment_id>/delete/', DeleteComment.as_view(), name='delete_comment'),
    path('comments/<uuid:comment_id>/like/', CommentLikeView.as_view(), name='like_comment'),
    
 

  
]
