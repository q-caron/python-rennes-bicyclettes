"""Modèles de l'app `bicyclettes`"""

from django.db import models
from django.urls import reverse


class Bicyclette(models.Model):
    """
    Une bicyclette, biclou ou vélo, c'est :
    un objet à deux roues et disposant d'une selle qui permet de se déplacer en pédalant.

    Fonctionne à l'énergie musculaire et peut disposer d'une assistance électrique.
    Une bicyclette est identifiée par un numéro unique.
    Possède un système de freinage qui permet de ralentir sa course, voire de la stopper.
    """

    class SystemesDeFreinage(models.TextChoices):
        """Le système de freinage permet de savoir quels éléments mécaniques permettent de ralentir le vélo."""

        V_BRAKE = ("VBR", "v-brake (patins sur roue)")
        DISQUES_MECANIQUE = ("DME", "à disques mécanique")
        DISQUES_HYDRAULIQUE = ("DHY", "à disques hydraulique")
        PATINS_HYDRAULIQUE = ("PHY", "à patins hydraulique")

    marque_et_modele = models.CharField(max_length=40, verbose_name="marque et modèle")
    identifiant_unique = models.CharField(max_length=20, verbose_name="identifiant unique", unique=True)
    a_une_assistance_electrique = models.BooleanField(default=False, verbose_name="a une une assistance électrique ?")
    systeme_de_freinage = models.CharField(max_length=3, verbose_name="systeme de freinage", choices=SystemesDeFreinage)

    class Meta:
        """Détails pour l'affichage d'instance ou du nom de la classe"""

        verbose_name = "bicyclettes"
        verbose_name_plural = "bicyclettes"

    def get_absolute_url(self):
        """
        Obtenir l'URL d'une instance de la classe en utilisant :
        - la vue 'bicyclettes:detail'
        - l'argument nommé identifiant_unique
        """
        return reverse("bicyclettes:detail", kwargs={"identifiant_unique": self.identifiant_unique})
