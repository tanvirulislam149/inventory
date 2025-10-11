from rest_framework.serializers import ModelSerializer, ValidationError
from Product.models import Product, Supplier, Category
from rest_framework import serializers

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    category = CategorySerializer() 
    supplier = SupplierSerializer()
    image_url = serializers.SerializerMethodField(method_name="get_image_url")
    
    class Meta:
        model = Product
        fields = ["id", "name", "price", "stock_quantity", "category", "supplier", "image_url"]

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url

class CreateProductSerializer(ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Product
        fields = ["name", "price", "stock_quantity", "category", "supplier", "image"]

    def validate_price(self, value):
        if value < 0:
            raise ValidationError("Price can't be negative")
        return value