from rest_framework.exceptions import ValidationError
# from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView # Django REST framework generic view for quick dev
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend # django-filters module with rest_framework provides filter backend feature.
from rest_framework.filters import SearchFilter # Build in Django Rest Framework, supports search backend
from rest_framework.pagination import LimitOffsetPagination

from store.serializers import ProductSerializer
from store.models import Product

class ProductsPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100 # max limit that can be set by API client

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',) # settings for DjangoFilterBackend : it enableds id filter: api/v1/products/?id=2
    search_fields = ('name', 'description') # settings for SearchFilter : to map query_params from url to serialized model data
    pagination_class = ProductsPagination

    # on_sale filter
    def get_queryset(self):
        on_sale = self.request.query_params.get('on_sale', None)
        if on_sale is None:
            return super().get_queryset()
        queryset = Product.objects.all()
        if on_sale.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now # to check if sale_start is before today and sale_end is after today, then product is on sale
            )
        return queryset

# CreateAPIView subclass
class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer
    
    # overwriting create fn
    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get('price')
            if price is not None and float(price) <= 0.0:
                raise ValidationError({ 'price': 'Must be above $0.0' }) # The validation is to make sure no one accidentally creates a Free product
        except ValueError:
            raise ValidationError({ 'price': 'A valid number is required' })
        return super().create(request, *args, **kwargs)

# DestroyAPIView
# class ProductDestroy(DestroyAPIView):
#     queryset = Product.objects.all()
#     lookup_field = 'id'

#     def delete(self, request, *args, **kwargs):
#         product_id = request.data.get('id')
#         response = super().delete(request, *args, **kwargs)
#         # above code is sufficient for destroying a product but it is also important to clear the cache for the specific product in models, below code is for that
#         if response.status_code == 204:
#             from django.core.cache import cache
#             cache.delete('product_data_{}'.format(product_id))
#         return response

# Combine Retrieve, Update and Destroy in one
class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        # above code is sufficient for destroying a product but it is also important to clear the cache for the specific product in models, below code is for that
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            product = response.data
            cache.set('product_data_{}'.format(product['id']), {
                'name': product['name'],
                'description': product['description'],
                'price': product['price']
            })
        return response