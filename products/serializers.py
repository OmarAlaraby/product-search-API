from rest_framework import serializers
from .models import Product, ProductBrand, ProductCategory

class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=ProductBrand.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=ProductCategory.objects.all())
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'brand', 'category']
        read_only_fields = ['id']
        depth = 1
        
        
    