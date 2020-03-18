# Django Portfolio

## 1. Project Setup
### 1.1 Creating Project
1. `django-admin startproject django_portfolio`: create project
2. rename root project folder name to 'django_portfolio_project' to avoid confusion with app folder name.
3. go to manage.py file path and run: `python3 manage.py runserver`

### 1.2 Creating a Django App
1. Difference b/w project and app: Project is the entire website. App is a specific module viz Events/blog/accounts
2. Create an app for jobs (Note: It is a good convention to always name your app in plural): `python3 manage.py startapp jobs`
3. Add the app to `INSTALLED_APPS` in **settings.py** file

### 1.3 Setting up URLs

## 2. Databases
### 2.1 Creating models
1. `image = models.ImageField(upload_to='images/')` Note for using ImageField we will have to install pillow if we haven't `pip3 install pillow`

### 2.2 Setting up Postgres
1. https://www.postgresql.org/ Download, install PostgreSQL 12
2. PostgreSQL 12: Server Settings: Make sure port is: 5432 (default) and Automatically start server is checked.
3. Click on start to initialize server
4. Double click on postgres. Will launch a terminal : #postgres
5. Change postgres password if needed : `\password postgres` enter password
6. Create Database: `CREATE DATABASE django_portfoliodb;` (Don't forget the semicolon)
7. will be able to see the newly created DB on PostgreSQL dashboard