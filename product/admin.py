from django.contrib import admin

# Register your models here.
"""
注册模型
"""
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
