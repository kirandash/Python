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

### 2.8 Controlling the number of formsets
1. Create the form we have to show while ordering multiple items
2. Also to save our data from form add: `filled_form.save()`. can be verified in admin