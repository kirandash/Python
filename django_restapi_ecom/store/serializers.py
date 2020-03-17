from rest_framework import serializers
from store.models import Product, ShoppingCartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')

class ProductSerializer(serializers.ModelSerializer):
    # overwriting serializer field
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2,max_length=200)
    cart_items = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end', 'is_on_sale', 'current_price', 'cart_items')

    # def to_representation(self, instance):
    #     data = super().to_representation(instance) # calling to_representation from parent
    #     data['is_on_sale'] = instance.is_on_sale() # is_on_sale of serialized data will be updated based on is_on_sale fn from models.py
    #     data['current_price'] = instance.current_price() # current_price fn from models.py
    #     return data # return data after projecting

    def get_cart_items(self, instance):
        items = ShoppingCartItem.objects.filter(product=instance)
        return CartItemSerializer(items, many=True).data