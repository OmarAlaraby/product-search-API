import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    min_calories = django_filters.NumberFilter(field_name='calories', lookup_expr='gte')
    max_calories = django_filters.NumberFilter(field_name='calories', lookup_expr='lte')
    is_vegan = django_filters.BooleanFilter()
    is_gluten_free = django_filters.BooleanFilter()
    brand = django_filters.CharFilter(field_name='brand__name', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = [
            'is_vegan',
            'is_gluten_free',
            'brand',
            'category',
        ]
