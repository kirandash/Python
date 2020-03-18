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

### 2.3 Connecting Django project to PostgreSQL DB
1. Change DATABASES settings in settings.py file. Replace sqlite settings with postgres settings
2. Note sqlite didn't need username and pswd bt postgres will need these additional settings. PostgreSQL is more robutst.
3. After adding settings compiler will through an error: **ModuleNotFoundError: No module named 'psycopg2'** To fix; `pip3 install psycopg2` (helps us to connect to postgres)
4. If the above throws erro: try: `pip3 install psycopg2-binary`
5. Run the server again to make sure there isn't any error and DB is connected properly

### 2.4 Migrations and migrate
1. Migrations helps us to migrate/save models to db
2. Run the command: `python3 manage.py makemigrations`: run this any time there is a new model or changes to an existing model
3. Create migrations folder in jobs/0001_initial.py
4. No need to touch files in migration folder
5. check all existing migrations: `python3 manage.py showmigrations` shows the new 0001_intitial migration and all the default migration files from django. [ ] prefix for the migration name means these are not applied yet.
6. Apply migration to all the models so far: `python3 manage.py migrate`
7. check migrations: `python3 manage.py showmigrations` [X] means the migrations are applied

### 2.5 Setting up admin panel and registering Job Model for admin
1. admin panel comes by default and added to the urlpattern.
2. To use the admin panel we will need a user. create a superuser: `python3 manage.py createsuperuser` (kiran, djangodb1234)
3. Login at http://localhost:8000/admin/
4. But admin yet doesn't show up the new Job model we created. To show that we have to let django know by editing the jobs/admin.py file
5. `admin.site.register(Job)`. Now the Job model will appear on dashboard

### 2.6 Creating Model objects via the admin panel
1. Go to admin
2. Click on Add icon next to Jobs model and add jobs (image and summary). It will create a new **Job Object** everytime we save a job detail.
3. Images will be uploaded to **django_portfolio/images** folder since we mentioned it in **jobs/models.py** file

### 2.7 Pulling objects from DB
1. `jobs = Job.objects` and `return render(request, 'jobs/home.html', {'jobs': jobs})` and html: `{% for job in jobs.all %}`

## 3. Designing
### 3.1 Bootstrap installation
1. Get HTML from view source: https://getbootstrap.com/docs/4.4/examples/album/
2. Get CSS and JS at: https://getbootstrap.com/docs/4.4/getting-started/introduction/ add it to head and script section.

### 3.2 Paye layout and templates adjustments

### 3.3 Adding static images to project
1. `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`
2. `urlPatterns = [] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)`
3. Note: Django will automatically collect all the files from static folders in project to be used in project

### 3.4 collectstatic
1. we have added image to jobs/static/logo.png : app level static folder
2. from manage.py folder run: `python3 manage.py collectstatic`. It will collect all the files from all the static folders in our apps and collectively put them in one place - a root level static folder. Note that it will add our image + static content from admin as well which comes by default.
3. static folder: static/admin, static/logo.png will be created
4. `{% load static %}` load static before head in html file
5. Add image to code `<img src="{% static 'logo.png' %}" height="200"/>`

### 3.5 Add bootstrap, jquery and popper as static asset
1. Bootstrap, jQuery and popper.js
2. https://getbootstrap.com/docs/4.4/getting-started/download/, https://jquery.com/download/, https://popper.js.org/
3. copy everything to jobs/static folder and to make it available, run command `python3 manage.py collectstatic`

### 3.6 Dynamic images from DB
1. Add MEDIA_URL and MEDIA_ROOT to settings.py file

## 4. Object Details
### 4.1 Connecting URLs and templates in Django
1. Proper labeling of job objects in admin