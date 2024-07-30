À la découverte de Django
=========================

Ce projet a été créé pour la présentation intitulée **Développer un site web ou solution métier avec Django : introduction**,
réalisée le mercredi 24 juillet 2024.

- 🔗 Lien vers l'évènement et les inscriptions : [Django Rennes art, Bashville swing](https://www.meetup.com/python-rennes/events/302163922/)
- 🔗 Lien vers le groupe de la communauté : [Meetup Python Rennes](https://www.meetup.com/python-rennes/)

# Informations pour la présentation
- Quentin Caron : Technical Lead chez Néosoft Rennes
- Profile LinkedIn : https://www.linkedin.com/in/qcaron/
- Présentation : Développer un site ou solution métier web avec Django : introduction
- Description :
  Django est un framework web Python vieux de 19 ans. Il est aujourd'hui le deuxième framework le plus populaire selon
  la Developer Survey 2023 de StackOverflow, juste derrière Flask et au coude-à-coude avec FastAPI sortit il y a 6 ans seulement.

  Je vais tenter de vous convaincre que Django est toujours, en 2024, un bon choix pour vos projets web surtout si vous
  ne souhaitez pas vous encombrer de React et consorts pour le côté front-end (👀 htmx).

  Je commencerai par vous présenter le framework afin de comprendre sa philosophie et son fonctionnement. Puis, nous
  construirons une application étape par étape, en suivant le paradigme _MVC_ (Model-View-Controller) ainsi qu'en
  manipulant une base de données `sqlite` via l'_ORM_ (Object Relational Mapper).

# Installer le projet

- installer poetry dans votre Python 3.12 : `python3 -m pip install poetry`
- créer l'environnement virtuel depuis la racine du projet : `python3 -m poetry install [--with dev]`

## Hooks `pre-commit`
Installez l'environnement virtuel avec l'option `--with dev` pour travailler facilement sur le projet en local.
Les dépendances telles que `pre-commit` et `pylint` seront ainsi installés et votre code sera vérifié à chaque commit.

Pour installer les hooks chez vous, vous devez exécuter la commande suivante : `poetry run pre-commit install`. Pour
en savoir plus, allez voir le fichier `.pre-commit-config` à la racine du projet et rendez-vous sur
[pre-commit.com](https://pre-commit.com/).

# Exécuter le projet

- à la récupération du projet, faire passer les migrations pour configurer la base de données locale (`sqlite`) : `poetry run python manage.py migrate`
- démarrer le serveur Django pour servir la web app en local : `poetry run python manage.py runserver`

# Pages disponibles
- accueil : http://localhost:8000/
   - liste des bicyclettes enregistrées avec un lien vers leur page de détail
   - bouton redirigeant vers la page / formulaire de création d'une bicyclette
- création de bicyclette : http://localhost:8000/bicyclettes/creer/
- détail d'une bicyclette : http://localhost:8000/bicyclettes/detail/<str:identifiant_unique>

# Plan de la présentation

1. Keskecé Django ?
   1. Django ce n'est pas... / C'est...
   2. Petite histoire de Django : 19 ans, de 2005 à 2024
   3. L'éco-système web Python
   4. Popularité des frameworks Python - Stack Overflow Dev Survey **2023** & Stack Overflow Dev Survey **2024**
   5. Répartition géographique des utilisateurs : JetBrains Django Developers Survey **2023**
   6. Popularité chez les développeurs : Et sur GitHub ?
   7. Versions et support Django : Pourquoi je l'ai recommandé à mon client ?
   8. Les avantages de Django
   9. Et ses inconvénients
2. Un peu de théorie
   1. Un bon vieux back-end - Requêtes et réponses HTTP
   2. Le paradigme MVC (MVT) - Model View Controller
   3. Le routage - Le liant du MVC/MTV
   4. Les gabarits, Langage de "templating" - Django Templating language
   5. L'API Queryset : manipuler les instances de modèles
   6. Les formulaires : Form : créer et modifier
   7. Un projet et des applications : Un code structuré
   8. Les commandes Django : Gérer votre projet et BDD
3. Mise en pratique : Activité de location de vélos : gestion d’un parc
   1. Créer le modèle Bicyclette
   2. Ajouter des champs du modèle
   3. Générer et exécuter les migrations
   4. Vérifier l’état de la base de données sqlite
   5. Gérer le modèle avec l’admin
   6. Visualiser le parc sur une page du site
   7. Templating et héritage
   8. Ajouter une page de création
   9. Créer une page de détail (bonus)
   10. Liens vers le dépôt GitHub
4. Et ensuite ?
   1. On n'a pas écrit de test 👋 mais bien sûr des choses existent : unittest ou pytest + pytest-django, requests factory...
   2. Et si on ne rafraîchissait pas tout l'écran à l'envoi du formulaire de création ? JSON Response et htmx
   3. Gérer une flotte de vélo : création en masse avec un formulaire non adossé à un modèle Django
   4. Plutôt qu'une simple liste, on pourrait afficher un tableau : django_tables2 app => illustrer encore une fois que des apps peuvent être intégrées
5. Conclusion
   1. Beaucoup de choses à apprendre : courbe d’apprentissage un peu raide
   2. Django est adapté à des besoins poussés et vous facilite les choses
   3. Et le paramétrage du projet ? Le déploiement ?
   4. La communauté est grande, les contributions nombreuses, le support assuré à long terme.

# Futures présentations ?
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
