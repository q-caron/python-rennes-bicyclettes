"""Routes de l'app `bicyclettes`"""

from django.urls import path

from bicyclettes.views import BicycletteCreateView, BicycletteDetailView

app_name = "bicyclettes"  # pylint: disable=C0103
urlpatterns = [
    path("detail/<str:identifiant_unique>", BicycletteDetailView.as_view(), name="detail"),
    path("creer/", BicycletteCreateView.as_view(), name="creer"),
]
