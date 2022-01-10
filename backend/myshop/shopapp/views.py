from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.filter(active = True)
    serializer_class = ProductSerializer

