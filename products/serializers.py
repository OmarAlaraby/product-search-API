from rest_framework import serializers
from .models import Product, ProductBrand, ProductCategory

class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']
    
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=ProductBrand.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=ProductCategory.objects.all())
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'brand', 'category', 'created_at',
            'serving_size', 'servings_per_container', 'calories', 'total_fat',
            'saturated_fat', 'trans_fat', 'cholesterol', 'sodium', 'total_carbohydrates',
            'dietary_fiber', 'sugars', 'added_sugars', 'protein', 'vitamin_d',
            'calcium', 'iron', 'potassium', 'ingredients', 'allergens',
            'is_vegan', 'is_gluten_free', 'is_organic'
        ]
        read_only_fields = ['id']


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        representation['brand'] = {
            'id': instance.brand.id,
            'name': instance.brand.name,
            'description': instance.brand.description
        }
        
        representation['category'] = {
            'id': instance.category.id,
            'name': instance.category.name,
            'description': instance.category.description
        }

        return representation
