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