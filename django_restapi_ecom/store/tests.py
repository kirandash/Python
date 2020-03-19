from rest_framework.test import APITestCase

from store.models import Product

class ProductCreateTestCase(APITestCase):
    def test_create_product(self): # testing if create product API works
        initial_product_count = Product.objects.count() # count before adding new product
        product_attrs = {
            'name': 'New Product',
            'description': 'Awesome product',
            'price': '123.45',
        } # new product attrs
        response = self.client.post('/api/v1/products/new', product_attrs) # adding new product
        if(response.status_code != 201):
            print(response.data)
        self.assertEqual(
            Product.objects.count(),
            initial_product_count + 1
        ) # check if new product count = earlier count + 1 ---> product added
        for attr, expected_value in product_attrs.items():
            self.assertEqual(response.data[attr], expected_value) # check if response data matches with the i/p data
        # also check if all the custom attrs have correct values
        self.assertEqual(response.data['is_on_sale'], False)
        self.assertEqual(
            response.data['current_price'],
            float(product_attrs['price']),
        )