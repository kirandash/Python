# Django COVID-19 Tracker

## Setup Django Project
### 1.1 What is Django
1. Django is a web framework built with Python. **Web Framework**: Collection of tools together in one package that we can use to build web applications.
2. **Django Features**: 
    - Object-Relational mapping (ORM) for DB Queries
    - URL routing: tells what logic to followe based on URL request on browser
    - HTML templating: for presentation logic
    - Form Handling
    - Testing
3. **Django is Not**:
    - A programming language. Python is. Django is a framework built with python and used for building websites.
    - A web server. Has a built in web server but only for dev purpose. Not for live website.
4. We will use Django for Only making DB Queries and creating APIs.
5. For frontend we will use React. The UI code is previously built at: https://github.com/kirandash/react/tree/master/covid-tracker. We will integrate our API on top of that.

### 1.2 Install Python and Django
1. **Python**: https://www.python.org/downloads/. Current version: 3.8.2. 
2. Download the .pkg file and run installation.
3. Check the version by typing `python3 --version`. (Python 3.8.2)
5. Python3 installs pip3 script to mac automatically. Note: for windows, use pip instead of pip3
6. **Install Django**: https://www.djangoproject.com/download/. Current version: 3.0.4
7. `pip3 install django==3.0.5` (will install django and pytz library which provides timezone support)

### 1.3 Create a Django project using django-admin
1. Django comes with a package called **django-admin** that helps us create django projects easily. So we don't have to setup everything from scratch.
2. `django-admin startproject django_covid_tracker`
3. Rename the folder name to django_covid_tracker_project to avoid confusion with the app name django_covid_tracker.

### 1.4 Understanding Folder structure
1. **manage.py**: 
    - Run Commands
2. **django_covid_tracker/__init__.py**: (aka Dunder Init file)
    - Tells Python that this folder contains Python files
3. **django_covid_tracker/wsgi.py and asgi**:
    - Provides hooks for web server viz apache or enginex when django is running on live web sites.
4. **django_covid_tracker/settings.py**:
    - Configures the Django Project
5. **django_covid_tracker/urls.py**:
    - Routes web requests based on URL
6. We will edit only the settings.py: to configure django and urls.py file to manage routes requests based on URL in this project.
7. Will Not Edit: manage.py, __init__.py, wsgi.py

### 1.5 Run Django Project
1. `cd django_covid_tracker_project`: folder with manage.py file. Since manage.py has all commands.
2. `python3 manage.py runserver` to run the project on local server. Ignore the warning about unapplied migrations. Note that this will also create a db.sqlite3 file, a local db file that django will use for running server.
3. Project will launch at http://127.0.0.1:8000/

### 1.6 Create a Django App
1. **Django Apps**:
    - A component in a Django Project
    - A folder with a set of Python files
    - Each app fits a specific purpose
    - Example: Blog, Forum, Wiki, In our project: countries (Single app)
4. `cd django_covid_tracker_project`: folder with manage.py file. Since manage.py has all commands.
5. `python3 manage.py startapp countries`: will create a django app or `django-admin startapp countries`
6. Add the created app to project. Go to django_covid_tracker/settings.py file ---> INSTALLED_APPS ---> Add `countries` to the end of preinstalled django apps. 

### 1.7 Understanding Django App Folder structure
1. **migrations/**: holds files to help us with migrate our DB when we change our schema over time. Or move code to different environment.
2. **__init__.py**: (Dunder Init file) - Tells Python that this folder contains Python files
3. **admin.py**: controls admin interface that can be used to edit data related to this app.
4. **apps.py**: controls settings specific to this app.
5. **models.py**: provides the data layer which Django uses to create DB schema or queries.
6. **tests.py**: Can add unit test for testing this app.
7. **views.py**: Holds logic and control flow for handling requests and defines HTTP response that can be returned.

### 1.8 Adding COVID Tracker UI to Workspace
1. The UI code is previously built at: https://github.com/kirandash/react/tree/master/covid-tracker. We will integrate our API on top of that later.

## 2. Django Models and the Admin
### 2.1 Models, routing, view and template
1. Django uses MVC architecture. (Model, View, Controller) Or MRVT. (Model, Route, View, Controller)
2. **MVC Architecture - Flow**:
    - URL Patterns ---> (Views --- Models) ---> Templates
3. In our project, we will use django only for creating Model and API. For view and URL routings, we will use React.

### 2.2 Models
1. Django Models helps us: 
    - Create the data layer of the Django App.
    - Define database structure.
    - Allows us to query the database.
4. **Model**: A model is a class inheriting from `django.db.models.Model` and it defines database fields as class attributes.
5. Our requirement: Countries with a name, country code, and other details.
6. Allow administrators to create, edit or delete countries.
7. Allow users to see a list of available dogs, with details about each one.
8. **countries/models.py** file: This contains the set of models for the django app.

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

### 2.4 Implement Country Model and add Fields
1. Open countries/models.py file. `from django.db import models`
2. Create a model Country(), a class inherited from django.models. `class Country(models.Model):`
3. Add country code and pinned Field to the model. Remaining data will be retrieved from API.

### 2.5 Migrations
**Keywords and definitions:**
1. **Models**: Defines the structure of database tables
2. **Migrations**: Generate scripts to change the database structure
3. **Intitial Migration**: By default no tables exists. So When a new model is defined, the **initial migration** will create the corresponding database tables
4. When is a migration needed? While adding a model. Or Adding a Field. Removing a Field. Or Changing a field.
5. **Migration commands**: `python3 manage.py makemigrations`, `python3 manage.py migrate`, `python3 manage.py showmigrations`
6. `makemigrations`:
    - Generates migration files for later use. 
    - Uses current model fields and current database tables
    - Creates numbered files in appname/migrations/
7. `migrate`:
    - Runs all migrations that haven't been run yet. To apply all migrations.
    - Can also run migrations for an app to a specific number using: `migrate <appname> <number>` eg `migrate countries 1`
8. **Unapplied migrations**: When a migration file has been created, but hasn't been run.
    - Very common source of error when working with a team. So always make sure to have a look at changing models and pull migration files.

**Running migrations on our project:**
1. Go to manage.py folder (`cd django_covid_tracker_project`, `ls`)
2. Run command: `python3 manage.py makemigrations` (creates model for countries app - Country model. Path: countries/migrations/0001_initial.py. It is called initial.py bcoz we don't have a table yet)
3. `python3 manage.py showmigrations` will list all the default django migrations along with countries migrations grouped. Note that the `[ ]` empty sq brackets imply that these migrations have not been applied so far.
4. Apply all migrations by running: `python3 manage.py migrate`. (Will show all applied migrations. 
5. Verify applied migrations by: Now running `showmigrations` command will show `[x]` for all the applied migrations)
6. Download os db tool: https://sqlitebrowser.org/: Helps us see sqlite db and their structures and contents.
7. Install sqlitebrowser. Launch from Applications/DB Browser for SQLite.
8. open database ---> select: db.sqlite3 file from our project.
9. Tables: countries_country + default django tables. Expanding each table,
10. Expand table countries_country to see all the fields we added to our db. code, pinned. By default id is added which is the unique key for our data.

### 2.6 Django Admin
1. open countries/admin.py file. create a CountryAdmin class by extending admin.ModelAdmin class - and add pass as content for making CountryAdmin a valid Python class, if there is no other code.
2. Create a superuser to work with db: `python3 manage.py createsuperuser` - username: kiran, pwd: common
3. Run server: `python3 manage.py runserver`
4. Server is available at: http://127.0.0.1:8000/admin/

### 2.7 Django list_display
1. By default the server will be showing list details of countries as Country object. We can control that with **list_display** attribute for model.

### 2.8 Query data with the Django ORM using shell
1. `python3 manage.py shell`: interactive python shell with django initialized
2. Press **ctrl + L** to clear screen in shell
3. `from countries.models import Country`
4. `Country.objects.all()`: returns all instances of the Country object model
5. `countries = Country.objects.all()`: to store it in a variable for continuous use
6. `country = countries[0]`
7. `country.code` or `country.pinned` or `country.id` etc
8. ctrl + l
9. `country = Country.objects.get(id=1)` is same as above for selecting the first Country
10. `country = Country.objects.get(id=2)` to select a different Country
11. `country = Country.objects.get(code='IN')` to select based on country code
11. `country = Country.objects.get(pinned=1)` exception: multiple results. multiple countries found (our code must take care of this exception)
12. `country = Country.objects.get(id=5555)` exception: Country does not exist (our code must take care of this exception)
13. `exit()`: to exit from shell