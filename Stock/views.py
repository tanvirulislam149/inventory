from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Stock.models import Stock
from Stock.serializers import StockSerializer

# Create your views here.
class StockViewset(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer