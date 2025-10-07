from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from Stock.models import Stock
from Product.serializers import ProductSerializer


class StockSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Stock
        fields = ["id", "product", "date", "quantity", "movement_type", "note"]
    