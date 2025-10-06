from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Product.models import Product, Category, Supplier
from Product.serializers import CategorySerializer, ProductSerializer, SupplierSerializer, CreateProductSerializer
from Core.permissions import IsStaff, IsOwner, IsOwnerOrStaff

# Create your views here.

class CategoryViewsets(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in ["DELETE"]:
            return [IsOwner()]
        return [IsOwnerOrStaff()]


class SupplierViewsets(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def get_permissions(self):
        if self.request.method in ["DELETE"]:
            return [IsOwner()]
        return [IsOwnerOrStaff()]


class ProductViewsets(ModelViewSet):
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.request.method in ["DELETE"]:
            return [IsOwner()]
        return [IsOwnerOrStaff()]


    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return CreateProductSerializer
        else: 
            return ProductSerializer