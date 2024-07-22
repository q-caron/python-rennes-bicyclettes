"""Administration de l'app `bicyclettes`"""

from django.contrib import admin

from .models import Bicyclette


@admin.register(Bicyclette)
class BicycletteAdmin(admin.ModelAdmin):
    """Admin pour Bicyclette"""

    list_display = (
        "identifiant_unique",
        "a_une_assistance_electrique",
    )
