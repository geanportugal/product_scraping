from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

from core.product.models import Product

from .serializers import ProductSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class WelcomeViewSet(viewsets.ViewSet):
    def list(self, request):
        content = "Fullstack Challenge 20201026"
        return Response(content)

class ProductModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    lookup_field = 'code'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
