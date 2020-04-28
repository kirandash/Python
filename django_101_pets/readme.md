# Django 101 - Building a Pets website

## Setup Django Project
### 1.1 What is Django
1. **Web Framework**: Collection of tools together in one package that we can use to build web applications.
2. Django is a web framework built with Python.
3. **Django Features**: 
    - Object-Relational mapping (ORM) for DB Queries
    - URL routing: tells what logic to followe based on URL request on browser
    - HTML templating: for presentation logic
    - Form Handling
    - Testing
4. **Django is Not**:
    - A programming language. Python is. Django is a framework built with python and used for building websites.
    - A web server. Has a built in web server but only for dev purpose. Not for live website.

### 1.2 Install Python and Django
1. **Python**: https://www.python.org/downloads/. Current version: 3.8.2. 
2. Download the .pkg file and run installation.
3. Check the version by typing `python3 --version`. (Python 3.8.2)
5. Python3 installs pip3 script to mac automatically. Note: for windows, use pip instead of pip3
6. **Install Django**: https://www.djangoproject.com/download/. Current version: 3.0.4
7. `pip3 install django==3.0.4` (will install django and pytz library which provides timezone support)
8. Upgrade pip: `sudo pip3 install --upgrade pip` (20.0.2)

### 1.3 Create a Django project using django-admin
1. Django comes with a package called **django-admin** that helps us create django projects easily. So we don't have to setup everything from scratch.
2. `django-admin startproject django_101_pets`

### 1.4 Understanding Folder structure
1. **manage.py**: 
    - Run Commands
2. **django_basics_dogs/__init__.py**: (aka Dunder Init file)
    - Tells Python that this folder contains Python files
3. **django_basics_dogs/wsgi.py and asgi**:
    - Provides hooks for web server viz apache or enginex when django is running on live web sites.
4. **django_basics_dogs/settings.py**:
    - Configures the Django Project
5. **django_basics_dogs/urls.py**:
    - Routes web requests based on URL
6. We will edit only the settings.py: to configure django and urls.py file to manage routes requests based on URL in this project.
7. Will Not Edit: manage.py, __init__.py, wsgi.py

### 1.5 Run Django Project
1. `cd django_101_pets`: folder with manage.py file. Since manage.py has all commands.
2. `python3 manage.py runserver` to run the project on local server. Ignore the warning about unapplied migrations. Note that this will also create a db.sqlite3 file, a local db file that django will use for running server.
3. Project will launch at http://127.0.0.1:8000/

### 1.6 Create a Django App
1. **Django Apps**:
    - A component in a Django Project
    - A folder with a set of Python files
    - Each app fits a specific purpose
    - Example: Blog, Forum, Wiki, In our project: adoptions (Single app)
4. `cd django_101_pets`: folder with manage.py file. Since manage.py has all commands.
5. `python3 manage.py startapp adoptions`: will create a django app or `django-admin startapp adoptions`
6. Add the created app to project. Go to django_101/settings.py file ---> INSTALLED_APPS ---> Add `adoptions` to the end of preinstalled django apps. 

### 1.7 Understanding Django App Folder structure
1. **migrations/**: holds files to help us with migrate our DB when we change our schema over time. Or move code to different environment.
2. **__init__.py**: (Dunder Init file) - Tells Python that this folder contains Python files
3. **admin.py**: controls admin interface that can be used to edit data related to this app.
4. **apps.py**: controls settings specific to this app.
5. **models.py**: provides the data layer which Django uses to create DB schema or queries.
6. **tests.py**: Can add unit test for testing this app.
7. **views.py**: Holds logic and control flow for handling requests and defines HTTP response that can be returned.

## 2. Django Models and the Admin
### 2.1 Models, routing, view and template
1. Django uses MVC architecture. (Model, View, Controller) Or MRVT. (Model, Route, View, Controller) (adoptions/models.py, django_101/urls.py, adoptions/views.py, adoptions/templates/)
2. **MVC Architecture - Flow**:
    - URL Patterns ---> (Views --- Models) ---> Templates
    - Files: django_101_kpets/urls.py ---> (adoptions/views.py --- adoptions/models.py) ---> adoptions/templates
    - Ex: http://bgwebagency.in/pets : "" ---> home() ---> home.html
    - Ex: http://bgwebagency.in/pets/1 : "/adoptions/1" ---> pet_detail() ---> pet_detail.html

### 2.2 Models
1. Django Models helps us: 
    - Create the data layer of the Django App.
    - Define database structure.
    - Allows us to query the database.
4. **Model**: A model is a class inheriting from `django.db.models.Model` and it defines database fields as class attributes.
5. Our requirement: Pet names with a name, age, vaccination record, and other details.
6. Allow administrators to create, edit or delete pets.
7. Allow users to see a list of available dogs, with details about each one.
8. **adoptions/models.py** file: This contains the set of models for the django app.

### 2.3 Django Fields
1. Each model can have multiple fields.
    - Ex: Dog Model will have the fields: name, submitter, submission_date, description etc.
2. **Field Types: Textual Data**: 
    - CharField
    - TextField
    - EmailField
    - URLField
3. **Field Types: Numeric Data**:
    - IntegerField : -1, 0, 20 etc
    - DecimalField
4. **Field Types: Decimal Data**:
    - BooleanField
    - DateTimeField : Date and Time combination
5. **Field Types: Relational Data**: For relationships b/w multiple models
    - ForeignKey: 1 (id of record in another table) Ex: model of user and model of songs. Model of user can contain a foreign key of song id to keep track of user's favorite song.
    - ManyToManyField: NA Ex: Vaccinations for dog. Many dogs can have one vaccination and lly many vaccinations for one dog.
6. Code Example: `model.CharField(max_length=10, blank=True)`
7. **Field Attribute Options**:
    - max_length
    - null (can have null or not)
    - blank (required or not)
    - choices (ex: Sex: Male or Female)
    - Read more at: https://docs.djangoproject.com/en/3.0/ref/models/fields/

### 2.4 Implement models and fields
1. Open adoptions/models.py file. `from django.db import models`
2. Create a model Pet(), a class inherited from django.models. `class Pet(models.Model):`
3. `vaccinations = models.ManyToManyField('Vaccine', blank=True)`

### 2.5 Migrations
Keywords and definitions:
1. Models: Defines the structure of database tables
2. Migrations: Generate scripts to change the database structure
3. Intitial Migration: By default no tables exists. So When a new model is defined, the **initial migration** will create the corresponding database tables
4. When is a migration needed? While adding a model. Or Adding a Field. Removing a Field. Or Changing a field.
5. Migration commands: `python manage.py makemigrations`, `python manage.py migrate`, `python manage.py showmigrations`
6. `makemigrations`:
    6.1 Generates migration files for later use. 
    6.2 Uses current model fields and current database tables
    6.3 Creates numbered files in appname/migrations/
7. `migrate`:
    7.1 Runs all migrations that haven't been run yet. To apply all migrations.
    7.2 Can also run migrations for an app to a specific number using:
    `migrate <appname> <number>` eg `migrate adoptions 1`
8. **Unapplied migrations**: When a migration file has been created, but hasn't been run.
    8.1 Very common source of error when working with a team. So always make sure to have a look at changing models and pull migration files.
Running migrations on our project:
1. Go to manage.py folder (`cd django_101_pets`, `ls`)
2. Run command: `python3 manage.py makemigrations` (creates model for adoptions app - Pet and vaccine model. Path: adoptions/migrations/0001_initial.py. It is called initial.py bcoz we don't have a table yet)
3. `python3 manage.py showmigrations` will list all the default django migrations along with adoptions migrations grouped. Note that the `[ ]` empty sq brackets imply that these migrations have not been applied so far.
4. Apply all migrations by running: `python3 manage.py migrate`. (Will show all applied migrations. 
5. Verify applied migrations by: Now running `showmigrations` command will show `[x]` for all the applied migrations)
6. Download os db tool: https://sqlitebrowser.org/: Helps us see sqlite db and their structures and contents.
7. Install sqlitebrowser. Launch.
8. open database ---> select: db.sqlite3 file from our project.
9. Tables: adoptions_pet, adoptions_vaccine, adoptions_pet_vaccinations (For Many To Many vaccinations field) + default django tables. Expanding each table, we can see all the fields we added to our db.

### 2.6 Import CSV data
1. Copy csv file to manage.py folder level
2. Copy management folder to adoptions folder. Contains commands to import csv file to db
3. Go to manage.py level. Run command: `python3 manage.py load_pet_data` (it will run the command load_pet_data.py and import csv into db)
4. Go to sqlitebrowser tool. Select adoptions_pet table and click on browse data to see the imported data
5. All these data is stored in db.sqlite3 file. So in case anytime there is an import error, we can always ask for db.sqlite3 file from a team member.

### 2.7 Django Admin
1. open adoptions/admin.py file. create a PetAdmin class
2. Create a superuser to work with db: `python3 manage.py createsuperuser`
3. Run server: `python3 manage.py runserver`
4. Server is available at: http://127.0.0.1:8000/admin/
5. By default the server won't be showing list details of pets properly. We can control that with **list_display** attribute for model.ModelAdmin and by configuring models.py __str__ fn for many to many model.

### 2.8 Query data with the Django ORM
1. `python3 manage.py shell`: interactive python shell with django initialized
2. Press **ctrl + L** to clear screen in shell
3. `from adoptions.models import Pet`
4. `Pet.objects.all()`: returns all instances of the Pet object model
5. `pets = Pet.objects.all()`: to store it in a variable for continuous use
6. `pet = pets[0]`
7. `pet.name` or `pet.description` or `pet.id` etc
8. ctrl + l
9. `pet = Pet.objects.get(id=1)` is same as above for selecting the first pet
10. `pet = Pet.objects.get(id=2)` to select a different pet
11. `pet = Pet.objects.get(age=1)` exception: multiple results (our code must take care of this exception)
12. `pet = Pet.objects.get(id=5555)` exception: does not exist (our code must take care of this exception)
13. For many to many: `pet = Pet.objects.get(id=7)` and `pet.vaccinations.all()`: will return QuerySet of all the vaccinations

## 3. Learning Django
### 3.1 Understand URL patterns
Definition
1. URL patterns dispatch request to views based on the path.
2. It uses regexp to interpret the urls for our site.
3. ducky: will match text ducky eg: rubber ducky, 
4. \d : d for digits: in this case 1 digit, 
5. \d+: d+ means one or more digit characters until anything other than digit eg: 12 ounces, it will match 12
6. ^admin/ : admin/inventory/item, : will match any characters that starts with admin/ but won't match the word admin/ itself
7. suffix$ : $ sign means end of sequence. so anything ending with suffix will be matched Eg: anything-suffix
8. Test your regexp at: https://pythex.org/

URL Patterns example: For project
1. url(regexp, view, name='index') eg: `url(r'^$', views.home, name='index')`: '^$' means empty string: no path. The 'r' tells python that the url string is a raw string. A raw string does not use \ as escape character.
2. once regexp matches 'views.home' will be loaded
3. name is used in templates
4. urlpatterns are evaluated from top to bottom until a match is found.

### 3.2 Implement URL patterns
1. `url(r'^adoptions/(\d+)/', views.pet_detail, name='pet_detail')`

### 3.3 Implement Django views
1. render function: `return render(request, 'pet_detail.html', {'pet': pet})`
2. 404 handling: `raise Http404('Pet not found')`

## 4. Django Templates
### 4.1 Intro
1. Django templates are basically HTML files with additional syntaxes.
2. Template syntax: `{{ variable }}`, `{%tag}`: template tags, `{{ variable|filter }}`: template filters

### 4.2 Implementation
1. Filter: `{{ pet.submission_date|date:"M d Y" }}`

### 4.3 Structure Templates

### 4.4 Add CSS and JS
1. define static directories to be used in settings.py file.
2. Next add static files to base.html file
3. `{% load static %}`
4. `{% static 'style.css' %}`: basepath/static/filename

## 5 Prod Release Notes
1. Debug: set to false
2. DB: PostgreSQL, MySQL etc. SQLite is mostly intended for dev work.