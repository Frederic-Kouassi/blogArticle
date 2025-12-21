
from django.contrib import admin
from django.urls import path
from blog.views import *
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name="index"),
     path("", liste_article, name="articles"),
     path("detail/<int:id>/", detail, name="detail"),
    path("articles/supprimer/<int:id>/", supprimer, name="supprimer_article"),
    path('modifier/<int:id>/', modifier_article, name='modifier'),
    path('user', create_users, name="user"),
    path("users/", liste_user, name="users"),
      path("login/", connexion, name="login"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
