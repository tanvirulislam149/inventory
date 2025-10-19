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
    stock_status = serializers.SerializerMethodField(method_name="get_stock_status")
    
    class Meta:
        model = Product
        fields = ["id", "name", "price", "stock_quantity", "category", "supplier", "image_url", "stock_status"]
    
    def get_stock_status(self, obj):
        if obj.stock_quantity == 0:
            return "Out of Stock"
        elif obj.stock_quantity < 15:
            return "Low Stock"
        else:
            return "In Stock"

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