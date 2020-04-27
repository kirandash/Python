# Django Basics
## 1. Intro
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
    - A programming language. Python is.
    - A web server. Has a built in web server but only for dev purpose.

### 1.2 Install Python and Django
1. **Python**: https://www.python.org/downloads/. Current version: 3.8.2. Download the .pkg file and run installation
2. Python also installs a package called pip3.
3. **Django**: https://www.djangoproject.com/download/. Current version: 3.0.5
4. `pip3 install Django==3.0.5`
5. Optional: pip upgrade if already existing: `pip3 install --upgrade pip`

### 1.3 Create a Django Project using django-admin
1. Django comes with a package called **django-admin** that helps us create django projects easily. So we don't have to setup everything from scratch.
2. `django-admin startproject django_basics_dogs`
3. Rename the project folder to django_basics_dogs_project to avoid confusion with similar app name.

### 1.4 Understanding Folder structure
1. **manage.py**: 
    - Run Commands
2. **django_basics_dogs/__init__.py**: (Dunder Init file)
    - Tells Python that this folder contains Python files
3. **django_basics_dogs/wsgi.py and asgi**:
    - Provides hooks for web server viz apache or enginex when django is running on live web sites.
4. **django_basics_dogs/settings.py**:
    - Configures the Django Project
5. **django_basics_dogs/urls.py**:
    - Routes web requests based on URL
6. We will edit only the settings.py and urls.py file in this course.
