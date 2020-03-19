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

class ProductDestroyTestCase(APITestCase):
    def test_delete_product(self):
        initial_product_count = Product.objects.count()
        product_id = Product.objects.first().id
        self.client.delete('/api/v1/products/{}/'.format(product_id)) # deleting a product
        self.assertEqual(
            Product.objects.count(),
            initial_product_count - 1
        ) # check if new product count = earlier count - 1 ---> product deleted
        self.assertRaises(
            Product.DoesNotExist,
            Product.objects.get, id=product_id
        ) # confirm that the product id does not exist in Product model anymore

class ProductListTestCase(APITestCase):
    def test_list_products(self):
        products_count = Product.objects.count()
        response = self.client.get('/api/v1/products/') # get all products
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous']) # making sure next and previous exists
        self.assertEqual(response.data['count'], products_count) # make sure the count prop has correct value
        self.assertEqual(len(response.data['results']), products_count) # make sure the length of results is correct count, no need to test each product since we are already testing individual product in different test case above