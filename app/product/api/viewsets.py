from rest_framework import mixins, viewsets
from app.product.models import Product
from .serializers import ProductSerializer

class ProductModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer