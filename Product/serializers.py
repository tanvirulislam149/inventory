from rest_framework.serializers import ModelSerializer
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
    class Meta:
        model = Product
        fields = "__all__"