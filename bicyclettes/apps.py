"""Configuration de l'application `bicyclettes`"""

from django.apps import AppConfig


class BicycletteConfig(AppConfig):
    """App config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "bicyclettes"
