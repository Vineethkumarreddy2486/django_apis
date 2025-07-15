from django.shortcuts import render
from .serializers import productSerializer
from .models import Product
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def product_list_create(request):
    if request.method == 'GET':
        product=Product.objects.all()
        serializer = productSerializer(product,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer=productSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def product_operations(request,id):
    try:
        product=Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({'error':'product not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer=productSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer=productSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)





