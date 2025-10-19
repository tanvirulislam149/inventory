from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Product.models import Product, Category, Supplier
from Product.serializers import CategorySerializer, ProductSerializer, SupplierSerializer, CreateProductSerializer
from Core.permissions import IsStaff, IsOwner, IsOwnerOrStaff
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

class CategoryViewsets(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', "description"]

    def get_permissions(self):
        if self.request.method in ["DELETE"]:
            return [IsOwner()]
        return [IsOwnerOrStaff()]


class SupplierViewsets(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['company_name', "person_name", 'phone', 'email']

    def get_permissions(self):
        if self.request.method in ["DELETE"]:
            return [IsOwner()]
        return [IsOwnerOrStaff()]


class ProductViewsets(ModelViewSet):
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['category',]
    search_fields = ["name"]

    queryset = Product.objects.select_related("supplier").select_related("category").all()

    def get_permissions(self):
        if self.request.method in ["DELETE"]:
            return [IsOwner()]
        return [IsOwnerOrStaff()]


    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return CreateProductSerializer
        else: 
            return ProductSerializer