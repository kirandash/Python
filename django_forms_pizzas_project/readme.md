# Django Forms

## 1. Getting Started witih Forms
### 1.1 Creating project
1. Install virtual environment: `pip3 install virtualenv`
2. Go to the directory where u want your project and Create a virtual environment: `virtualenv anyname` or `virtualenv django_restapi_ecom_env`
3. Activate virtual environment: `source django_restapi_ecom_env/bin/activate`. It should show that we are in the virtual env in terminal. (django_restapi_ecom_env)
4. Install django: `pip3 install django`
5. Create a django project: `django-admin startproject django_forms_pizzas` This will create the project.
6. Rename to root project name to 'django_forms_pizzas_project' to avoid confusion with the app name 'django_forms_pizza'
7. `cd django_forms_pizzas_project` and Run server: `python3 manage.py runserver`
8. Project will run at: http://localhost:8000/

### 1.2 Making Forms from scratch - Create App and add URLs
1. Create a django app called pizza: `django-admin startapp pizza`.
2. Add app name to INSTALLED_APPS array in settings.py file.
3. Add urls to home page and order page to urlpatterns in urls.py file. `path('', views.home, name='home'), path('order', views.order, name='order')`

### 1.2 Making Forms from scratch - Add views to the App
1. Create views for home and order page in pizza/views.py
2. Create templates at pizza/templates/pizza

### 1.3 Form fields - For order page
1. Create form in order.html template