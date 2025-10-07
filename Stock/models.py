from django.db import models
from Product.models import Product

# Create your models here.
class Stock(models.Model):
    MOVEMENT_TYPE = {
        "IN": "IN",
        "OUT": "OUT"
    }
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stock")
    date = models.DateField(auto_now_add=True)
    movement_type = models.CharField(choices=MOVEMENT_TYPE, default="IN")
    quantity = models.PositiveIntegerField()
    note = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.product_name} X {self.movement_type}"
