"""Formulaires de l'app `bicyclettes`"""

from django import forms

from bicyclettes.models import Bicyclette


class BicycletteForm(forms.ModelForm):
    """Pour la gestion des bicyclettes"""

    class Meta:
        """Définition du modèle Django et champs à utiliser"""

        model = Bicyclette
        fields = (
            "marque_et_modele",
            "identifiant_unique",
            "a_une_assistance_electrique",
            "systeme_de_freinage",
        )
