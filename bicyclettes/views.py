"""Vues de l'app `bicyclettes`"""

from django.views.generic import CreateView, DetailView

from bicyclettes.forms import BicycletteForm
from bicyclettes.models import Bicyclette


class BicycletteCreateView(CreateView):
    """Création d'une nouvelle bicyclette"""

    model = Bicyclette
    form_class = BicycletteForm


class BicycletteDetailView(DetailView):
    """Voir la fiche d'information d'une bicyclette"""

    model = Bicyclette
    context_object_name = "bicyclette"
    slug_field = "identifiant_unique"
    slug_url_kwarg = "identifiant_unique"
