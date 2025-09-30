from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Product.models import Product, Category, Supplier
from Product.serializers import CategorySerializer, ProductSerializer, SupplierSerializer

# Create your views here.

class CategoryViewsets(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SupplierViewsets(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductViewsets(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer