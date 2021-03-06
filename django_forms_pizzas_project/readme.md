# Django Forms

## 1. Getting Started witih Forms
### 1.1 Creating project
1. Install virtual environment: `pip3 install virtualenv`
2. Go to the directory where u want your project and Create a virtual environment: `virtualenv anyname` or `virtualenv django_restapi_ecom_env`
3. Activate virtual environment: `source django_restapi_ecom_env/bin/activate`. It should show that we are in the virtual env in terminal. (django_restapi_ecom_env)
4. Install django: `pip3 install django`
5. Create a django project: `django-admin startproject django_forms_pizzas` This will create the project.
6. Rename to root project name to 'django_forms_pizzas_project' to avoid confusion with the app name 'django_forms_pizza'
7. `cd django_forms_pizzas_project` and Run server: `python3 manage.py runserver`. Note: we can specify port number as: `python3 manage.py runserver 8080`
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

### 1.4 Submitting Forms
1. default action is current url. Good practice to always mention even if it's default.
2. form method="get" or "post". Get request adds the form data to url on submission. while post method doesn't.
3. For post method of submission, we will get an error 'CSRF verification failed. Request aborted.' To fix this add `{% csrf_token %}` to form.

### 1.5 Django Form Class
1. Django Form class helps us building forms in a much easier way than the manual html way of building it.
2. create pizza/forms.py and add Form class to it.
3. Code: `item2 = forms.CharField(label='Item 2', max_length=100) size = forms.ChoiceField(label='Size', choices=[('Small Size', 'Small'), ('Medium Size'), ('Large Size')])`
4. pass form class to order.html template from views.py ex: `return render(request, 'pizza/order.html', {'orderform', form})`

### 1.6 Using Submitted a Data
1. Handle GET and POST method differently on views.py
2. Send note from views.py to order.html and display on template

## 2. Advanced Form Features
### 2.1 Adding Models
1. Data from form will now be stored in db. For that we will need to create the models.
2. Define the models in pizza/models.py page.
3. Register the new classes to show on admin page by adding `admin.site.register(Order)` on pizza/admin.py file
4. Since we have done model changes - let's run migrate commands.
5. `python3 manage.py makemigrations`
6. `python3 manage.py showmigrations` to see the list of migrations available. [ ] prefix means the migration is not applied.
7. To apply run: `python3 manage.py migrate`
8. `python3 manage.py showmigrations` to see the list of migrations available. [X] prefix means the migrations are applied.
9. Create a superuser to access admin: `python3 manage.py createsuperuser` username: kiran password: mycommonpwd
10. Go to admin: http://localhost:8000/admin/ and add sizes. Since sizes should be added by admin: http://localhost:8000/admin/pizza/size/add/. Once added all sizes can be seen at: http://localhost:8000/admin/pizza/size/. Note that size info is properly shown at http://localhost:8000/admin/pizza/size/ because of the `def __str__(self): return self.title` code we added to the models.py file.

### 2.2 Model Forms
1. Once the model is available, we can use the same model to create multiple forms. By saving time.
2. Let's replace the Django Form Class in forms.py with Django Model Form class
3. And create a subclass called Meta which will hold all our form meta info like model, fields, labels

### 2.3 Widgets
1. `widget = forms.Textarea` and `widget = forms.PasswordInput` Ex: `item1 = forms.CharField(label='Item 1', max_length=100, widget = forms.Textarea)`
2. Multiple selection widget: `items = forms.MultipleChoiceField(choices=[('i1', 'Item1'), ('i2', 'Item2'), ('i3', 'Items3')], widget=forms.CheckboxSelectMultiple)`

### 2.4 Advanced Widgets
1. We can also use widgets with ModelForm class in pizza/forms.py file.

### 2.5 Forms & Files
1. Add `enctype="multipart/form-data"` to form in order.html for form to accept files
2. `pip3 install pillow` to be able to work with images
3. Add image field to OrderForm class in forms.py file: `image = forms.ImageField()`
4. To be able to accept files in view: get `request.FILES` from OrderForm in views.py file

### 2.6 Formsets: Multiple forms on a page
1. Formsets allows us to take one form and repeat over and over

### 2.7 Formset Views
1. Add items view to views.py file.

### 2.8 Controlling the number of formsets and saving to DB
1. Create the form we have to show while ordering multiple items
2. Also to save our data from form add: `filled_form.save()`. can be verified in admin

### 2.9 Editing order Objects:
1. Add url `path('order/<int:pk>', views.edit_order, name='edit_order'),`
2. Create edit_order fn

### 2.10 Input Confirmation:
1. Create edit_order.html to hold the edit order form.

### 2.11 Module 2 Quiz
1. Why Formsets?\
Ans: Formsets allows us to take one form and repeat over and over
2. In order to accept files in a form, what must you add to the form?\
Ans: `enctype="multipart/form-data"`
3. ModelForm?\
Ans: ModelForm helps us to create forms from our existing models.

## 3. Customizing and Styling Form Appearance
### 3.1 Local validation and errors:
1. So far the validations are only at browser level. But not server level.
2. Note that the fields are required by default and adds additional validations as per field type viz email, url etc
3. To avoid default html validation, use `novalidate` with form tag in order.html page.

### 3.2 Server based erros
1. Add server based validation in views.py.

### 3.3 Form Rendering - as_p
1. `as_p` displays form tags with paragraph ex: `{{ orderform.as_p }}`
2. `as_table`: surround with `<table>` tag
3. `as_ul`: surround with `ul` tag or `ol` tag

### 3.4 Customizing Forms
1. We can customize individual fields Ex: `{{ orderform.item1.errors }} {{ orderform.item1.label_tag }} {{ orderform.item1 }}`

### 3.5 Forms with CSS - django-widget-tweaks
1. Will use bootstrap
2. `pip3 install django-widget-tweaks`, add `widget_tweaks` to settings.py apps list
3. getbootstrap.com - docs - starter template
4. use template in order.html page
5. load widgets app in order.html `{% load widget_tweaks %}`
6. We can add custom class to fields with widget tweaks: `{% render_field field class="form-control" %}`

### 3.6 Creating Base HTML and Extend order HTML from it
1. navigation: `href="{% url 'home' %}"`
2. create base.html file with block: `{% block 'body' %} {% endblock %}`
3. extend order.html from base.html file: `{% extends 'pizza/base.html' %} {% block 'body' %} {% endblock %}`

### 3.7 Styling Home page and extending other pages from base.html
1. Extend home.html from base.html
2. For images: add static root to settings.py file: `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`
3. Add image to pizza/static folder
4. Every time there is a new image or file added we have to run collectstatic command: `python3 manage.py collectstatic`. It will collect all the files from all the static folders in our apps and collectively put them in one place - a root level static folder. Note that it will add our image + static content from admin as well which comes by default.
5. use `{% load static %}` in home.html page to load static files.
6. extend pizzas.html from base.html and edit_order.html page

### 3.8 Module 3 - Quiz
1. How to show errors for one field in a form?\
Ans: `form.field.error`
2. How to display form in paragraph tags?\
Ans: `.as_p`