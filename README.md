À la découverte de Django
=========================

# Information pour la présentation
- Quentin Caron : Technical Lead chez Néosoft Rennes
- Profile LinkedIn : https://www.linkedin.com/in/qcaron/
- Présentation : Développer un site ou solution métier web avec Django : introduction
- Description :
  Django est un framework web Python vieux de 18 ans. Il est aujourd'hui le plus populaire d'entre eux selon
  la Developer Survey 2023 de StackOverflow, coude-à-coude avec FastAPI sortit il y a 6 ans seulement.

  Je vais tenter de vous convaincre que Django est toujours, en 2024, un bon choix pour vos projets web surtout si vous
  ne souhaitez pas vous encombrer de React et consorts pour le côté front-end (👀 htmx).

  Je commencerai par vous présenter le framework afin de comprendre sa philosophie et son fonctionnement. Puis, nous
  construirons une application étape par étape, en suivant le paradigme _MVC_ (Model-View-Controller) ainsi qu'en
  manipulant une base de données `sqlite` via l'_ORM_ (Object Relational Mapper).

# Installer le projet

- installer poetry dans votre Python 3.12 : `python3 -m pip install poetry`
- installer poetry depuis la racine du projet : `python3 -m poetry install --with dev`

# Exécuter le projet

- à la récupération du projet, faire passer les migrations pour configurer la BDD : `poetry run python manage.py migrate`
- démarrer le serveur Django pour servir la web app en local : `poetry run python manage.py runserver`

# Plan de la présentation

1. Keskecé Django ?
   1. Django c'est...
   2. L'éco-système web Python => info Stack Overflow Dev Survey 2023
   3. Petite histoire de Django => 18 ans, de 2006 à 2024, avec la Fondation et versions
   4. Les avantages du framework
   5. Pourquoi continuer à l'utiliser ?
2. Un peu de théorie
   1. Un bon vieux back-end => requêtes et réponses HTTP
   2. Le paradigmes MVC et MVT
   3. Le routage
   4. Le langage de templating (gabarits)
   5. L'API Queryset
   6. Les formulaires
   7. Un projet avec des apps
   8. Les commandes `django-admin` / `manage`
   9. Poster, avec notions non abordées (middlewares, authentification, messages, signaux...)
3. Mise en pratique
   1. Créer un environnement virtuel : `python -m venv` ou `poetry init`
   2. Installer Django : `pip install Django` ou `poetry add Django`
   3. Démarrer un projet Django : `django-admin startproject les_bo_velos`
   4. Créer une application `main` : `python manage.py startapp bicyclettes`
   5. Créer une première page : créer une route, une vue, un template
   6. Utiliser un modèle dans la page web : créer un modèle, ajouter une QuerySet au contexte
   7. Filtrer les données : créer un modelform, ajouter le form au template, gérer le form dans la vue
   8. Et l'admin !
4. Et ensuite ?
   1. Et si on ne rafraîchissait pas tout l'écran à l'envoi du formulaire de création ? JSON Response et htmx
   2. On n'a pas écrit de test 👋 mais bien sûr des choses existent : unittest ou pytest + pytest-django, requests factory...
   3. Gérer une flotte de vélo : création en masse avec un formulaire non adossé à un modèle Django
   4. Plutôt qu'une simple liste, on pourrait afficher un tableau : django_tables2 app => illustrer encore une fois que des apps peuvent être intégrées
5. Conclusion
   1. Réflexion portée sur le métier : "model-first" => vous gérez de la connaissance métier, il faut y adhérer et se l'approprier
   2. Implémentation étape par étape, relativement guidée si l'on suit la documentation : models, view, urls, admin
   3. Batteries included : requêtes, réponses, ORM, templating, admin...
   4. Des apps à disposition pour mettre en forme les pages web (crispy forms) et enrichir le projet (django_tables2)
   5. Gestion des utilisateurs : il y a bien plus avec les groupes et les permissions
   6. Futures présentations ?

# Déroulé

## 1. Keskecé Django ?

- Framework web Python
- Première version en 2006 pour un journal américain  ==> ce qui explique popularité du framework aux États-Unis ?
- Les objectifs et avantages du framework
- La Django Foundation : avenir du framework, documentation (versions et langues)...
- Où en est le framework aujourd'hui ? Pourquoi continuer à l'utiliser ?
- Les concurrents de Django : éco-système web Python (Flask, Pyramid, FastAPI)

## 2. Un peu de théorie

- Web : requêtes et réponses HTTP
- Structure : _project_ (projet) et _apps_ (applications)
- Le paradigme _MVC_ (Model View Controller) ou plutôt MVT (Model View Template)
- Le _routing_ (routage)
- Les _templates_ (gabarits) et le langage Django
- Les _forms_ et _model forms_ (formulaires et formulaire pour les modèles)
- L'ORM (Object Relationnal Mapper)
- L'API QuerySet
- L'authentification : _users_ (utilisateurs), _groups_ (groupes) et _permissions_ (permissions)
- Les _settings_ (paramétres)
- Les commandes `django-admin` / `manage`:
    - gestion des utilisateurs (createsuperuser) ==> utilisateurs admin
    - migrations (makemigrations, migrate)
- La sécurité : protection contre les injections SQL, les failles CSRF, XSS, clickjacking...

## 3. Mise en pratique

Étapes de la démo :
1. L'application a un objectif : servir le métier. Les loueurs de vélo gèrent un parc => créer un modèle Bicyclette => Créer une classe qui a une docstring et lui donner une Meta
2. Ajouter les champs : caractères, booléens, à choix limités ou unique
3. Le modèle est prêt : créons la table en BDD les commandes Django makemigrations et migrate
4. Créer des vélos en se connectant à la base sqlite locale
5. Pas terrible. Créons l'administration de notre modèle et d'abord créer un superuser. Visite guidée...
6. Comment visualiser ces bicyclettes sur le site ? Création de l'accueil du site => function-base view et template accueil
7. Simplifions le template en créant un template de base pour faire de l'héritage
8. Avec un formulaire de création c'est mieux non ? Form adossé au modèle, CBV, url
9. Fiche de détail d'un vélo : DetailedView

## 4. Et ensuite ?
1. Et si on ne rafraîchissait pas tout l'écran à l'envoi du formulaire de création ? JSON Response et htmx
2. On n'a pas écrit de test 👋 mais bien sûr des choses existent : unittest ou pytest + pytest-django, requests factory...
3. Gérer une flotte de vélo : création en masse avec un formulaire non adossé à un modèle Django
4. Plutôt qu'une simple liste, on pourrait afficher un tableau : django_tables2 app => illustrer encore une fois que des apps peuvent être intégrées

## 5. Conclusion
1. Réflexion portée sur le métier : "model-first" => vous gérez de la connaissance métier, il faut y adhérer et se l'approprier
2. Implémentation étape par étape, relativement guidée si l'on suit la documentation : models, view, urls, admin
3. Batteries included : requêtes, réponses, ORM, templating, admin...
4. Des apps à disposition pour mettre en forme les pages web (crispy forms) et enrichir le projet (django_tables2)
5. Gestion des utilisateurs : il y a bien plus avec les groupes et les permissions
6. Futures présentations ?

Futures présentations ?
- Les _groups_ (groupes) et _permissions_ (permissions)
- Les _signals_ (signaux)
- Les _middlewares_ (intergiciels)
- Exploiter l'_admin_ Django
- Les commandes `django-admin` et `manage`:
    - Gestion des données (dump, load, flush)
    - Gestion des fichiers statiques (collectstatic)
- La sécurité : CSRF
- API avec DRF (Django Rest Framework)
- Les templates : langage Django avec ses _template tags_ + Jinja2
- Django Debug Toolbar (DjDT)
- Afficher des tableaux facilement avec django_tables2
- Wagtail
- Une stack complète sous Docker / Docker-compose avec PostgreSQL + Local AWS S3

# Cas pratique : loueur de vélos

Projet cycle : maintenance d'un parc de vélo

- Obligations légales :
  - casque homologué obligatoire pour les enfants jusque 12 ans
  - gilet de haute visibilité "rétroréfléchissant" homologué (marquage "CE")
  - sonnette en bon état
  - éclairage fonctionnel
  - freins avant et arrière
  - VAE : limite à 25km/h, assistance déclenchée au pédalage, moteur de 250W maximum

- Points de sécurité:
  - pneumatiques : craquelures ou usure (structure visible)
  - freinage : fonctionnel et en bon état, attention à l'usure (patins, plaquettes, machoires, disques, roue (piste de freinage), câbles, gaînes, huile)
  - serrage : tous les éléments serrés au bon couple
  - graissage et huilage : gaînes, potence, axes, selle
  - propreté : boues ou cailloux (bloquage des rouges ou de la chaîne)

- Amendes :
  - non-port du casque pour les enfants de moins de 12 ans : jusqu'à 750 €. En général, il s'agit d'une amende forfaitaire de 135 €. L'adulte qui transporte l'enfant ou qui l'accompagne doit s'en assurer.
  - non-port du gilet rétroréfléchissant : jusqu'à 150 €. En général, il s'agit d'une amende forfaitaire de 35 €.
  - éclairage obligatoire : jusqu'à 38 €. En général, il s'agit d'une amende forfaitaire de 11 €.
  - freins obligatoires : jusqu'à 38 €. En général, il s'agit d'une amende forfaitaire de 11 €.
  - sonnette : jusqu'à 38 €. En général, il s'agit d'une amende forfaitaire de 11 €.
  - marquage obligatoire
