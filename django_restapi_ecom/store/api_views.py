from rest_framework.generics import ListAPIView # Django REST framework generic view for quick dev

from store.serializers import ProductSerializer
from store.models import Product

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer