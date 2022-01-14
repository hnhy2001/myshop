from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=11)
    role =  models.CharField(max_length=50)
    cart = models.ManyToManyField('Product', blank=True, null=True)

class Product(models.Model):
    product_name = models.CharField(max_length=250, null=False, unique=True)
    avatar = models.ImageField(upload_to='img/%Y/%m')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    product_price = models.FloatField(null=False)
    active = models.BooleanField(default=True)

class Order(models.Model):
    order_price = models.FloatField(null=False)
    product_id = models.ManyToManyField(Product, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Notication(models.Model):
    active = models.BooleanField(default=True)
    content = models.TextField()
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)




