"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from core.product.api.viewsets import ProductModelViewSet, WelcomeViewSet


router = routers.DefaultRouter()
router.register(r'products',ProductModelViewSet)
router.register(r'', WelcomeViewSet, basename='welcome')

schema_view = get_schema_view(title='Open Food Prodcuts API')

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='Open Food Prodcuts API')),
    path('schema/', schema_view),
]
