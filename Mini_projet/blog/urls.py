from django.urls import path
from blog.views import home, about, contact, admin_dashboard, user_dashboard, RegisterView, LoginView, VerifyEmailView

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path("user-dashboard/", user_dashboard, name="user_dashboard"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("verify-email/", VerifyEmailView.as_view(), name="verify_email"),
]
