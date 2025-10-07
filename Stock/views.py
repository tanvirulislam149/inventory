from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Stock.models import Stock
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