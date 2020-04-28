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