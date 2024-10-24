from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product
from product.serializer import CatagorySerializer, ProductSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['POST'])
def create_catagory(request):
    catagory_serializer = CatagorySerializer(data=request.data)
    if catagory_serializer.is_valid():
        catagory_serializer.save()
        return Response(catagory_serializer.data, status=status.HTTP_201_CREATED)
    return Response(catagory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_catagory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    catagory_serializer = CatagorySerializer(category, data=request.data)
    if catagory_serializer.is_valid():
        catagory_serializer.save()
        return Response(catagory_serializer.data, status=status.HTTP_200_OK)
    return Response(catagory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_catagory(request,category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_all_catagory(request):
    listCatagory = Category.objects.all()
    catagory_serializer = CatagorySerializer(listCatagory, many=True)
    return Response(data=catagory_serializer.data, status=status.HTTP_200_OK)

############################################################################################################

@api_view(['POST'])
def create_product(request):
    product_serializer = ProductSerializer(data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)
    return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['PUT'])
def update_product(request, product_id):
    category = get_object_or_404(Category, id=product_id)
    product_serializer = ProductSerializer(category, data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_200_OK)
    return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_all_product(request):
    listProduct = Product.objects.all()
    product_serializer = ProductSerializer(listProduct, many=True)
    return Response(data=product_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_product_by_name(request, name):
    products = Product.objects.filter(name__icontains=name)
    if products.exists():
        product_serializer = ProductSerializer(products, many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "No products found with the given name"}, status=status.HTTP_404_NOT_FOUND)