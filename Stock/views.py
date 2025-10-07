from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Stock.models import Stock
from Product.models import Product
from Stock.serializers import StockSerializer, CreateStockSerializer

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
        serializer.save()
        data = serializer.data
        product = Product.objects.filter(id=data["product"]).first()
        print("product", product)
        if data["movement_type"] == "IN":
            product.stock_quantity = product.stock_quantity + data["quantity"]
        elif data["movement_type"] == "OUT":
            product.stock_quantity = product.stock_quantity - data["quantity"]
            
        product.save()
