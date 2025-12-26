from django.urls import path
from blog.views.home_view import home, about, contact, admin_dashboard, user_dashboard


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path("user-dashboard/", user_dashboard, name="user_dashboard"),
]
