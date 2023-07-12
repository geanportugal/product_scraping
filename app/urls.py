from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from app.product.api.viewsets import ProductModelViewSet


router = routers.DefaultRouter()
router.register(r'products',ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
