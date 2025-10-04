from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name 

class Supplier(models.Model):
    company_name = models.CharField(max_length=100)
    person_name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.company_name} | {self.person_name}" 

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    supplier = models.ManyToManyField(Supplier, related_name="products")
    image = CloudinaryField("image", default="default_mlcgud")

    def __str__(self):
        return self.name