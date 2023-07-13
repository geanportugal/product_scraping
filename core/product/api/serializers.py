from rest_framework import serializers
from core.product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['code', 'barcode', 'status', 'imported_t', 'url', 
                 'product_name', 'quantity',  'categories', 'packaging', 
                 'brands', 'image_url' ]
