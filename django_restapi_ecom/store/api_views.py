from rest_framework.generics import ListAPIView # Django REST framework generic view for quick dev
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
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