# Django 101 - Building a Pets website

## Setup Django Project
### 1.1 What's Django?
Django provides:
1. ORM (Object-relational Mapping): for querying database
2. URL routing
3. HTML templating
4. Form handling
5. Testing

Django is Not:
1. A programming lang. A framework built with python and used for building websites.
2. A web server. Only has a dev web server. Not for live website.

### 1.2 Install Python and Django
1. Install python from https://www.python.org/. Check the version by typing `python3 --version`. (Python 3.8.2)
2. Python3 installs pip3 script to mac automatically. Note: for windows, use pip instead of pip3
3. Install Django: `pip3 install django==3.0.4` (will install django and pytz library which provides timezone support)
4. Upgrade pip: `sudo pip install --upgrade pip` (20.0.2)

### 1.3 Create a Django project
1. `django-admin.py startproject django_101_pets`
Project Structure:
1. manage.py: Runs commands
2. __init__.py (aka Dunder init file): Tells Python that the folder contains Python files
3. wsgi.py: Provides hook for web servers viz apache
4. settings.py: configures django
5. urls.py: Routes requests based on URL

Will Not Edit:
1. manage.py, __init__.py, wsgi.py

Will Edit:
1. settings.py: to configure django, urls.py: routes requests based on URL

Start Project:
1. `cd django_101_pets`
2. `python3 manage.py runserver` to run the project on local server. Ignore the warning about unapplied migrations.
3. Project will launch at http://127.0.0.1:8000/