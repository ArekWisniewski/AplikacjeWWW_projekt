from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import View


@api_view(['POST'])
def category_create(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def category_detail(request, pk):
    if request.method == 'GET':
        categories = Category.objects.get(pk=pk)
        serializer = CategorySerializer(categories)
        return Response(serializer.data)


@api_view(['PUT'])
def category_update(request, pk):
    if request.method == 'PUT':
        categories = Category.objects.get(pk=pk)
        serializer = CategorySerializer(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def category_delete(request, pk):
    if request.method == 'DELETE':
        categories = Category.objects.get(pk=pk)
        categories.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def customer_create(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def customer_detail(request, pk):
    if request.method == 'GET':
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


@api_view(['PUT'])
def customer_update(request, pk):
    if request.method == 'PUT':
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def customer_delete(request, pk):
    if request.method == 'DELETE':
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def products_create(request):
    if request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def products_search(request, query):
    if request.method == 'GET':
        products = Products.objects.filter(name__icontains=query)
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def products_detail(request, pk):
    if request.method == 'GET':
        products = Products.objects.get(pk=pk)
        serializer = ProductsSerializer(products)
        return Response(serializer.data)


@api_view(['PUT'])
def products_update(request, pk):
    if request.method == 'PUT':
        products = Products.objects.get(pk=pk)
        serializer = ProductsSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def products_delete(request, pk):
    if request.method == 'DELETE':
        products = Products.objects.get(pk=pk)
        products.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def order_create(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def order_list(request):
    if request.method == 'GET':
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def order_detail(request, pk):
    if request.method == 'GET':
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


@api_view(['PUT'])
def order_update(request, pk):
    if request.method == 'PUT':
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def order_delete(request, pk):
    if request.method == 'DELETE':
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
