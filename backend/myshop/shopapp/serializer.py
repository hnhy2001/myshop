from rest_framework.serializers import ModelSerializer
from .models import User, Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'avatar', 'product_price']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'phone', 'cart']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.role = "user"
        user.save()
        return user

