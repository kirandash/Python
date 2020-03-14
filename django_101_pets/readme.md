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
1. `cd django_101_pets`: folder with manage.py file. Since manage.py has all commands.
2. `python3 manage.py runserver` to run the project on local server. Ignore the warning about unapplied migrations. Note that this will also create a db.sqlite3 file, a local db file that django will use for running server.
3. Project will launch at http://127.0.0.1:8000/

### 1.4 Create a Django App
1. An App is a folder with python files
2. Within django, an app is a component
3. Each app fits a specific purpose. Eg: Blog / Forum / Wiki
4. `cd django_101_pets`: folder with manage.py file. Since manage.py has all commands.
5. `python3 manage.py startapp adoptions`: will create a django app
6. Add the created app to project. Go to django_101/settings.py file ---> INSTALLED_APPS ---> Add `adoptions` to the end of preinstalled django apps. 

App Folder Structure:
1. apps.py: Configuration & Initialization
2. models.py: Data layer
3. admin.py: Administrative interface
4. urls.py: URL routing
5. views.py: Control layer
6. tests.py: Tests the app
7. migrations/: Holds the migration files (for db migrating)

## 2. Django Models and the Admin
### 2.1 Models, routing, view and template
1. Django uses MVC architecture. Or MRVT. (adoptions/models.py, django_101/urls.py, adoptions/views.py, adoptions/templates/)

### 2.2 Models
1. A Model helps us: Create the data layer of the app, Define DB structure, To query db.
2. models.py file: This contains the set of models for the django app.
3. Model: A model is a class inheriting from django.db.models.Model, and is used to define fields as class attributes.

### 2.3 Fields
1. Numeric data: IntegerField, DecimalField
2. Textual data: CharField, TextField, EmailField, URLField
3. Miscellaneous data: BooleanField, DateTimeField
4. Relational data: ForeignKey, ManyToMany
Ex: `models.CharField(max_length=10, null=True, blank=True)`
Field attributes: max_length, null, blank, default, choices
Doc: https://docs.djangoproject.com/en/3.0/ref/models/fields/

### 2.4 Implement models and fields
1. `from django.db import models`
2. `class Pet(models.Model):`
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