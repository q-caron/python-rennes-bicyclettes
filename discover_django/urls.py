"""URLs pour le projet"""

from django.contrib import admin
from django.urls import include, path

from main import views as accueil_views

urlpatterns = [
    path("", accueil_views.accueil, name="accueil"),
    path("bicyclettes/", include("bicyclettes.urls", namespace="bicyclettes")),
    path("admin/", admin.site.urls),
]
