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
3. `pip3 install django-filter`: for filtering backend data
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

### 2.4 Filter backends with URL query params
1. `from django_filters.rest_framework import DjangoFilterBackend`, use `DjangoFilterBackend` for straight field filters
2. can check at http://localhost:8000/api/v1/products/?id=2
3. For complicated filters with more logic, use `get_queryset` function
4. can check at http://localhost:8000/api/v1/products/?on_sale=true

### 2.5 Enabling full-text search filter back end
1. Search through product names and descriptions
2. **SearchFilter**: Filter back end built into Django REST Framework
3. can be checked at http://localhost:8000/api/v1/products/?search=mineral
4. Search types: Partial Match (default), Exact match, Regular Expression ex: $[Ee]ar$

### 2.6 Enabling pagination of querysets in API responses
1. Django can limit querysets in 3 ways:

    1.1 PageNumber pagination: use a pagenumber to paginate results
    
    1.2 LimitOffset pagination: Use a limit and offset fields to more finely paginate results.
    
    1.3 Cursor pagination: Use a DB cursor to paginate results (Recommended for larger database. Since other 2 are inefficient)

2. can verify at: http://localhost:8000/api/v1/products/?limit=2&offset=1
3. It also returns a next prop which tells which api to call next to get next set of data. Ex: "http://localhost:8000/api/v1/products/?limit=2&offset=3"

### 2.7 Quiz:
1. Which method in a Serializer sub-class do we override to add extra data to a serialized response?

    Ans: `to_representation`

2. **ListAPIView:** The ListAPIView is the generic Django REST Framework view used to serialize a list of objects into a JSON API response.
3. Django REST Framework API views can be created with the as_view method in the URLs configuration just like regular Django views. Django REST Framework maintains some API compatibility with Django’s views, and this is one case where they implement the same method.
Ex: `path('api/v1/products/', store.api_views.ProductList.as_view()),`
4. When using Django Filters with a serializer, what is the name of the configuration variable that sets which fields are used to filter the queryset data?

    Ans: `filter_fields`: The filter_fields variable on a serializer will add the field as a URL query parameter and will filter the queryset of objects using those fields specified.
5. Searching through text fields on a model is built into Django REST Framework. The search backend, unlike the filter backend, is built into Django REST Framework.
6. What are the classes of Pagination available for paginating an API view?

    Ans: There are three built in types of pagination available with Django REST Framework. **PageNumberPagination, LimitOffsetPagination, and CursorPagination**

    Cursor pagination is the best performance choice for paginating large data sets. Page number and limit offset pagination are good for small- to medium-sized data sets. However, only cursor pagination (which uses the databases cursor) is efficient enough for large data sets.

## 3. CRUD operations for Models
### 3.1 Creating a CreateAPIView subclass
1. Data Source (Excel Spreadsheet / XML / JSON / Other DB) ---> Imported through REST API ---> Populating the DB 

### 3.2 Connecting a CreateAPIView to the router
1. Add path to urlpatterns `path('api/v1/products/new', store.api_views.ProductCreate.as_view()),`
2. run server `python3 manage.py runserver`
3. Run curl command in terminal: `curl -X POST http://localhost:8000/api/v1/products/new -d price=1.00 -d name='My Product' -d description='Hello World'`: will return a response with product details i.e. just created
4. Dev team shared curl scripts to create quick models and test if REST API is working correctly
5. We can also test the same on browser: visiting http://localhost:8000/api/v1/products/new (Django's tool for easy CRUD testing)