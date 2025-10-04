from rest_framework.serializers import ModelSerializer, ValidationError
from Product.models import Product, Supplier, Category

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
    supplier = SupplierSerializer(many=True)
    class Meta:
        model = Product
        fields = ["id", "name", "price", "stock_quantity", "category", "supplier"]

class CreateProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "stock_quantity", "category", "supplier"]

    def validate_price(self, value):
        if value < 0:
            raise ValidationError("Price can't be negative")
        return value