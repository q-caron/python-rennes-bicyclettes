"""Administration de l'app `bicyclettes`"""

from django.contrib import admin

from .models import Bicyclette


@admin.register(Bicyclette)
class BicycletteAdmin(admin.ModelAdmin):
    """Admin pour Bicyclette"""

    list_display = (  # Seules ces colonnes seront affichées sur la page listant les bicyclettes
        "identifiant_unique",
        "a_une_assistance_electrique",
    )
