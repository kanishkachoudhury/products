from rest_framework import serializers
from product.models import Product, Category

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['prodName', 'prodPrice', 'prodDescription', 'category']


