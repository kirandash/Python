from rest_framework import serializers
from store.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end')

    def to_representation(self, instance):
        data = super().to_representation(instance) # calling to_representation from parent
        data['is_on_sale'] = instance.is_on_sale() # is_on_sale of serialized data will be updated based on is_on_sale fn from models.py
        data['current_price'] = instance.current_price() # current_price fn from models.py
        return data # return data after projecting

