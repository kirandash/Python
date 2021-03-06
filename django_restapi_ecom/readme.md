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

### 3.3 Creating a DestroyAPIView subclass
1. Delete a product and clear cache

### 3.4 Connecting a DestroyAPIView to the router
1. Add path to urlparameter
2. Visit url on browser http://localhost:8000/api/v1/products/5/destroy and click delete button
3. Create a product `curl -X POST http://localhost:8000/api/v1/products/new -d price=5 -d name='Water Bottle' -d description='This bottle is amazing'` check all the products at http://localhost:8000/api/v1/products/
4. Delete it: `curl -X DELETE http://localhost:8000/api/v1/products/7/destroy` check all the products at http://localhost:8000/api/v1/products/

### 3.5 RetrieveUpdateDestroyAPIView to Creating an UpdateAPIView subclass and retrieve + delete
1. RetrieveUpdateDestroyAPIView helps us Reuse Django REST framework generic view instead of calling GET, POST, PUT, DELETE etc separately
2. We can reuse code and configuration
3. Example: the serializer_class or queryset can be reused
4. One URL can be used to handle multiple HTTP methods.
5. The generic RetrieveUpdateDestroyAPIView combines the “get”, “put”, “patch”, and “delete” HTTP methods into one API view.

### 3.6 Connecting an UpdateAPIView to the router
1. Add path to urlpatterns and visit http://localhost:8000/api/v1/products/1/ and can do update, delete or retrieve and check results at http://localhost:8000/api/v1/products/

### 3.7 Quiz
1. The ValidationError can be raised with an error message for a specific field by passing in a dictionary.

    Code:

    `from rest_framework.exceptions import ValidationError`

    `raise ValidationError({ 'price': 'Must be above $0.0' })`

2. Where is the HTTP method handled urls.py or api view?

    Ans: The HTTP method isn't handled in the URL configuration. It’s part of the API view class where methods are defined for each type of HTTP method.

3. In a DestroyAPIView, we can override the delete method to additionally clean up the cache, delete other models or record statistics. The HTTP method used by DestroyAPIView is “delete” and can be overridden to add more functionality such as cache clean-up after an object is destroyed.

4. The generic RetrieveUpdateDestroyAPIView combines the “get”, “put”, “patch”, and “delete” HTTP methods into one API view.

5. When using the RetrieveUpdateDestroyAPIVIew, the URL path pattern must include a model instance id or primary key. The primary key or id in the URL is used to identify the model instance that will be acted on.

## 4. Managing Serializer fields, relations and validation
### 4.1 Serializer with only selected fields
Serializer field configuration:
1. **read_only**: whether or not the field can be written to through the serializer
2. **source**: where the data for the serializer field will be populated from ex: `product_name=serializers.CharField(source='name')`
3. **min_length, max_length**

### 4.2 Serializer that shows model relationships
1. **SerializerMethodField**: get_ is the prefix to the field name for the method that is called.
2. Serializer for one or many instances: **many=True** creates a list of serialized model instances
3. **many=false** (default) will serialize only one model instance
4. try in shell: `python3 manage.py shell` (We will add 5 of product id 1 to shopping cart and then return the JSON)
5. >>>`import json`
6. >>>`from store.models import *`
7. >>>`from store.serializers import *`
8. >>>`product = Product.objects.all().first()`
9. >>>`cart = ShoppingCart()`
10. >>>`cart.save()`
11. >>>`item=ShoppingCartItem(shopping_cart=cart, product=product, quantity=5)`
12. >>>`item.save()`
13. >>>`serializer=ProductSerializer(product)`
14. >>>`print(json.dumps(serializer.data, indent=2))`

### 4.3 Number fields with serializers
1. IntegerField(min_value, max_value)
2. FloatField(min_value, max_value)
3. DecimalField(min_value, max_value, max_digits, decimal_places): has more control compared to the FloatField
4. Test by editing values at: http://localhost:8000/api/v1/products/1/

### 4.4 DateTimeField configuration
1. **input_formats**: for Date/Time i/p formats: default: ISO-8601 ex: "2020-03-29T12:01:56.000000Z"
2. **format**: o/p format: default: DateTime object
3. **help_text**: appears in browser for the REST API
4. **style**: controls how field appears in browser for REST API (eg input and placeholder styling)
5. Add the sale_start and sale_end fields to serializers.py file. http://localhost:8000/api/v1/products/1/
6. Acceptable input ex: sale_start: "11:05 PM 16 Mar 2020", saved in ISO-8601. Note: if any error is thrown after saving, just reload the page. The saved data will show up

### 4.5 Lists, Dicts and JSON objects
1. Creating a serializer to show stats. This won't be a model serializer.
2. The stats will hold daily sales of a particular product.

### 4.6 Serializer with ImageField and FileField
Show photo field in JSON and add warranty file content to product description field if a file is uploaded.
1. Serializer settings: Note that all serializer fields are read_only bydefault. But if a field is not present in the model, we should set it as write_only true. But note that it will not be saved in model.
2. **validated_data**: This data has already passed through serializer and model validation process. It is used to create or update a model.

### 4.7 Module 4 Quiz
1. How to make sure a serializer field is read only?

    Ans: `serializers.BooleanField(read_only=True)`

2. All number serializer fields, IntegerField, FloatField and DecimalField can be constrained with min_value and max_value.

3. DateTimeField serializer field can accept custom i/p format for the date and time.

4. For DictField serializer field, value can be any data type and key must be a string.

5. Example of composite fields: DictField, ListField

6. write-only field in model serializer is used: when the field is used to populate other model fields

## 5. Testing API Views
### 5.1 Test case for CreateAPIView subclass with APITestCase
1. Django REST framework has 4 types of API test cases: APISimpleTestCase, APITransactionTestCase, APITestCase, APILiveServerTestCase
2. **APITestCase**: 

    2.1 All of the test case classes implement the same interface as Django's TestCase class

    2.2 Note: Use the JSON format when testing API client requests: `self.client.post(url, data, format='json')`
3. REST APIs with custom data:
    
    3.1 REST APIs can return custom data fields that are created through serializer fields or through overriding the to_representation method
    
    3.2 Ex: is_on_sale, current_price are updated from method calls

    3.3 Important to thorougly test custom data to ensure it's correct: one untested field can cause API consumers and clients to fail or crash

4. Run test: `python3 manage.py test`: This will fail if sale_start and sale_end is not made optional. Please modify serializers.py file accordingly. and run `python3 manage.py test`. New error: `unexpected keyword argument warranty` which means warranty is not mentioned as a part of the create method. Fix this by implementing create method and removing warranty from the validated_data. Run the test again and now everything should pass

### 5.2 Test case for DestroyAPIView subclass
1. Note: in production projects, make sure to test that cleanup methods are executed when destroying the model through API. Ex: clear caches, destory the object in other 3rd-party services

### 5.3 Test case for ListAPIView subclass
1. Add test fn and run `python3 manage.py test`

### 5.4 Test case for UpdateAPIView subclass
1. Update API View is failing. Fix that by updating API view properly in serializers.py file

### 5.5 Test case for image upload in UpdateAPIView subclass

### 5.6 Module 5 Quiz
1. Django REST Framework HTTP client for testing implements the same interface as Django HTTP client
2. Django REST Framework APITestCases for testing has the same interface from the Django TestCase unit testing class
3. Response of paginated ListAPIView: results
4. Unit test for UpdateAPIView, which HTTP methods to use: PATCH and PUT
5. When writing unit test to test ImageField or FileField, the format of HTTP request must be "multipart" than "json"

### 5.7 Next Reads:
1. Designing RESTful APIs
2. Advanced web development with Django
3. Consume API with React