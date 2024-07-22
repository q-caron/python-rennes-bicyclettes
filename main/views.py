"""Vues exploitant diverses applications installées dans le projet"""

from django.shortcuts import render

from bicyclettes.models import Bicyclette


def accueil(request):
    """La page d'accueil de notre site"""
    return render(
        request,
        "main/accueil.html",
        {
            "bicyclettes": Bicyclette.objects.all(),
        },
    )
