from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.utils import json

from .models import Product, User
from .serializer import ProductSerializer, UserSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.filter(active = True)
    serializer_class = ProductSerializer

    @action(methods=['post'],detail=False)
    def search(self, request):
        count = request.data["count"]
        product = Product.\
            objects.\
            filter(product_name__icontains = request.data["content"],
                   id__range = [count*1, count*10] )
        return Response(ProductSerializer(product, many=True).data,
                        status=status.HTTP_200_OK)

    @action(methods=['post'],detail=False)
    def products(self, request):
        list = request.data["products"]
        product = Product.\
            objects.\
            filter(id__in = list)
        return Response(ProductSerializer(product, many=True).data,
                        status=status.HTTP_200_OK)

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active = True)
    serializer_class = UserSerializer
    @action(methods=['post'],detail=False)
    def login(self, request):
        user = User.\
            objects.\
            filter(username = request.data["username"], password = request.data["password"])
        return Response(UserSerializer(user, many=True).data,
                        status=status.HTTP_200_OK)

    @action(methods=['post'],detail=False, url_path="cart")
    def cart(self, request):
        id = request.META["HTTP_ID"]
        user = User.objects.filter(id = int(id), is_active = True)
        product = Product.objects.filter(pk = request.data["product_id"])
        user.cart.add(product)
        user.save()
        return Response(UserSerializer(user, many=True).data,
                        status=status.HTTP_200_OK)