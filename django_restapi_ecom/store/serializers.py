from rest_framework import serializers
from store.models import Product, ShoppingCartItem

class CartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')

class ProductSerializer(serializers.ModelSerializer):
    # overwriting serializer field
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2,max_length=200)
    cart_items = serializers.SerializerMethodField()
    # price = serializers.FloatField(min_value=1.00, max_value=100000)
    price = serializers.DecimalField(
        min_value=1.00, max_value=100000,
        max_digits=None, decimal_places=2
    )
    sale_start = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'], format=None, 
        allow_null=True, help_text='Accepted format is "12:01 PM 19 March 2020"',
        style={'input_type': 'text', 'placeholder': '04:01 PM 23 March 2020'}
    )
    sale_end = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'], format=None, 
        allow_null=True, help_text='Accepted format is "12:01 PM 19 March 2020"',
        style={'input_type': 'text', 'placeholder': '04:01 PM 23 March 2020'}
    )

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

class ProductStatSerializer(serializers.Serializer):
    # A composite serializer
    stats = serializers.DictField( # dictionary of stats
        child = serializers.ListField( # list of dates
            child=serializers.IntegerField() # no of products sold in a day - all sales listed in an array
        )
    )