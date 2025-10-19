from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Stock.models import Stock
from Product.models import Product, Category, Supplier
from Stock.serializers import StockSerializer, CreateStockSerializer
from rest_framework.exceptions import ValidationError
from django.db import transaction
from Core.permissions import IsOwner, IsOwnerOrStaff
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Sum, Q

# Create your views here.
class StockViewset(ModelViewSet):
    queryset = Stock.objects.select_related("product").select_related("user").select_related("product__category").select_related("product__supplier").all()

    def get_permissions(self):
        if self.request.method in ["DELETE", "PUT", "PATCH"]:
            return [IsOwner()]
        return [IsOwnerOrStaff()]

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return CreateStockSerializer
        else: 
            return StockSerializer
        
    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save(user = self.request.user)
            data = serializer.data
            product = Product.objects.filter(id=data["product"]).first()
            print("product", product)
            if data["movement_type"] == "IN":
                product.stock_quantity = product.stock_quantity + data["quantity"]
            elif data["movement_type"] == "OUT":
                if product.stock_quantity < data["quantity"]:
                    print("check quantity")
                    raise ValidationError(f"The requested quantity of this product is not available. Only {product.stock_quantity} product is available.")
                product.stock_quantity = product.stock_quantity - data["quantity"]

            product.save()



class DashboardViewset(ModelViewSet):
    http_method_names = ["get"]
    permission_classes = [IsOwnerOrStaff]

    def list(self, request):
        data = {
            "product_count": Product.objects.aggregate(Sum("stock_quantity")),
            "category_count": Category.objects.count(),
            "supplier_count": Supplier.objects.count(),
            "out_of_stock": Product.objects.filter(stock_quantity__lt=15).count()
        }
        return Response(data)


class RecentActivitiesViewset(ModelViewSet):
    http_method_names = ["get"]
    permission_classes = [IsOwnerOrStaff]
    serializer_class = StockSerializer
    queryset = Stock.objects.order_by("date").all()[:5]