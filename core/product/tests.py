from django.test import TestCase

from django.test import TestCase
from rest_framework.test import APIClient
from core.product.models import Product
from core.product.api.serializers import ProductSerializer
from core.product.api.viewsets import StandardResultsSetPagination, ProductModelViewSet


class ProductModelViewSetTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(code='123455699989889', 
                                              product_name='Test Product', 
                                              url='https://example.com/123455699989889')

    def test_list_products(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        products = ProductSerializer(Product.objects.all(), many=True).data
        self.assertEqual(response.data, products)

    def test_retrieve_product(self):
        response = self.client.get("/products/{}/".format(self.product.code))
        self.assertEqual(response.status_code, 200)
        product = ProductSerializer(self.product).data
        self.assertEqual(response.data, product)