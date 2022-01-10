from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'avatar', 'created_date', 'product_price', 'active']

admin.site.register(Product, ProductAdmin)