# Django - Building RESTful web APIs - ecommerce website
## 1 Intro
### 1.1 Project details
1. Libraries: Mock, for creating mocks in the unit tests
2. Pillow, for image editing

## 2 Serializing, Listing, Filtering and paginating models
### 2.1 Creating a Django Rest Framework serializer to serialize a model
Setup:
1. Create project: `django-admin.py startproject django_restapi_ecom`
2. Install reqd modules: `pip3 install djangorestframework`
3. `pip3 install django-filter`
4. `pip3 install Pillow`: for image uploader
5. Migrations: `python3 manage.py makemigrations`, `python3 manage.py migrate`
6. store folder is previously setup for this project. Includes store models.
7. Create Virtual environment: `sudo pip install virtualenv` and `virtualenv django_restapi_ecom_env`

Serializing:
1. Serialization formats: JSON, YAML, XML
2. Product Model --> Serialize it to JSON --> Served through REST API
3. Serializing product model fields: Id, Name, Price, Sale start date, Sale end date
4. Make sure vir env is created.
5. Activate vir env: `source django_restapi_ecom_env/bin/activate`
6. move to manage.py path
7. Initiate django shell (A useful tool for rapid prototyping and testing): `python3 manage.py shell`
8. >>> `from store.models import Product`
9. >>> `product = Product.objects.all()[0]`
10. >>> `from store.serializers import ProductSerializer`
11. >>> `serializer = ProductSerializer()`
12. >>> `data = serializer.to_representation(product)`
13. >>> `from rest_framework.renderers import JSONRenderer`
14. >>> `renderer = JSONRenderer()`
15. >>> `print(renderer.render(data))` This is to finally render the serialized data

### 2.2 Creating a ListAPIView subclass
1. Product serializer ---> List API view ---> Products List returned from our API
2. Django REST framework generic views: **ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView**: Django provides these generic views that help speed up dev work.
3. Note: Most cases: Use Django REST framework's generic API views and mixins. Rare cases: use base APIView to build up the API from the ground up

### 2.3 Connecting an APIView to a route
1. open django_restapi/urls.py file
2. Add path to urlpatterns: `path('api/v1/products/', store.api_views.ProductList.as_view())`
3. Run server: `python3 manage.py runserver`
4. Check the REST API at: http://localhost:8000/api/v1/products/