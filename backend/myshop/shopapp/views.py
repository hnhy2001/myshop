from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets,status,generics
from .models import Product
from .serializer import ProductSerializer

def hello(request):
    return HttpResponse("hello")

class ProductView(viewsets.ViewSet, generics.ListAPIView):
    queryset = Product.objects.filter(active = True)
    serializer_class = ProductSerializer

