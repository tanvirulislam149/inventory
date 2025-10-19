from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from Product.models import Product, Supplier, Category
from Stock.models import Stock 
from django.contrib.auth import get_user_model

User = get_user_model()

class SimpleSupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "company_name"]

class SimpleCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class SimpleProductSerializer(ModelSerializer):
    category = SimpleCategorySerializer()
    supplier = SimpleSupplierSerializer()
    image_url = serializers.SerializerMethodField(method_name="get_image_url")

    class Meta:
        model = Product
        fields = ["id", "name", "price", "stock_quantity", "image_url", "category", "supplier"]
    
    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url


class SimpleUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]

class StockSerializer(ModelSerializer):
    product = SimpleProductSerializer()
    user = SimpleUserSerializer()

    class Meta:
        model = Stock
        fields = ["id", "product", "date", "quantity", "movement_type", "note", "user"]

class CreateStockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = ["id", "product", "date", "quantity", "movement_type", "note"]
    