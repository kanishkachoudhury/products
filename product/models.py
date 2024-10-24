from django.db import models


class Category(models.Model):
    catName = models.CharField(max_length=100, unique=True)
    catDescription = models.TextField(max_length=200)

class Product(models.Model):
    prodName = models.CharField(max_length=100)
    prodPrice = models.DecimalField(max_digits=10,decimal_places=2)
    prodDescription = models.TextField(max_length=200)
    # 1 catogory many product, 1:M
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
