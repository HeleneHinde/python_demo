# README

Ce projet est une application Django nommée `python_demo`.

## Prérequis
- Python 3.12 ou supérieur
- pip
- (Optionnel) virtualenv

## Installation

1. **Cloner le dépôt**

```zsh
git clone <url-du-repo>
cd python_demo
```

2. **Créer et activer un environnement virtuel** (optionnel mais recommandé)

```zsh
python3 -m venv venv
source venv/bin/activate
```

3. **Installer les dépendances**

```zsh
pip install django
```

4. **Appliquer les migrations**

```zsh
python manage.py migrate
```

5. **Lancer le serveur de développement**

```zsh
python manage.py runserver
```

Le site sera accessible sur [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Structure du projet

- `manage.py` : Script principal de gestion Django
- `blog/` : Application principale (modèles, vues, templates, static)
- `python_demo1/` : Configuration du projet Django
- `db.sqlite3` : Base de données SQLite

## Commandes utiles

- Créer un superuser :
  ```zsh
  python manage.py createsuperuser
  ```
- Accéder à l’admin : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Personnalisation

- Les fichiers CSS/JS sont dans `blog/static/blog/`
- Les templates HTML sont dans `blog/templates/blog/`

## Tests

Pour lancer les tests :
```zsh
python manage.py test blog
```

## Auteur
HeleneHinde
