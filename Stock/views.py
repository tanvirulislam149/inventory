from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Stock.models import Stock
from Product.models import Product
from Stock.serializers import StockSerializer, CreateStockSerializer
from rest_framework.exceptions import ValidationError
from django.db import transaction

# Create your views here.
class StockViewset(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return CreateStockSerializer
        else: 
            return StockSerializer
        
    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()
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
