
from django.contrib import admin
from django.urls import path
from blog.views import index, liste_article, detail,supprimer, modifier_article, create_user
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name="index"),
     path("", liste_article, name="articles"),
     path("detail/<int:id>/", detail, name="detail"),
    path("articles/supprimer/<int:id>/", supprimer, name="supprimer_article"),
    path('modifier/<int:id>/', modifier_article, name='modifier'),
    path('user', create_user, name="user"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
