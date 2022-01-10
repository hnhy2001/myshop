from rest_framework.serializers import ModelSerializer
from .models import User, Product

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'avatar', 'product_price']