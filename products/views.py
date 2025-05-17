from rest_framework import viewsets
from .models import Product, ProductBrand, ProductCategory
from .serializers import ProductSerializer, ProductBrandSerializer, ProductCategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter

# utils
from django.db.models import Q
from decouple import config
import deepl
from functools import reduce
import operator
from langdetect import detect

# docs 
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.query_params.get('search', None)

        if keyword:
            translator = deepl.Translator(config('DEEPL_API_KEY'))
            translated = translator.translate_text(keyword, target_lang="EN-US")

            print(keyword, translated)
            search_fields = [
                "name", "description", "brand__name", "brand__description", "category__name",
                "category__description", "ingredients", "allergens", "serving_size", "calories", "total_fat",
                "saturated_fat", "trans_fat", "cholesterol", "sodium", "total_carbohydrates", "dietary_fiber",
                "sugars", "added_sugars", "protein", "vitamin_d", "calcium", "iron", "potassium",
            ]

            
            queries = [
                Q(**{f"{field}__icontains": keyword}) | Q(**{f"{field}__icontains": translated})
                for field in search_fields
            ]
            
            combined_query = reduce(operator.or_, queries)
            queryset = queryset.filter(combined_query).distinct()

        return queryset
    
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'search', openapi.IN_QUERY,
                description="Search across product fields (with translation)",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'is_vegan', openapi.IN_QUERY,
                description="Filter by vegan status",
                type=openapi.TYPE_BOOLEAN
            ),
            openapi.Parameter(
                'is_gluten_free', openapi.IN_QUERY,
                description="Filter by gluten-free status",
                type=openapi.TYPE_BOOLEAN
            ),
            openapi.Parameter(
                'brand', openapi.IN_QUERY,
                description="Filter by brand name",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'category', openapi.IN_QUERY,
                description="Filter by category name",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'min_calories', openapi.IN_QUERY,
                description="Minimum calories",
                type=openapi.TYPE_NUMBER
            ),
            openapi.Parameter(
                'max_calories', openapi.IN_QUERY,
                description="Maximum calories",
                type=openapi.TYPE_NUMBER
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ProductBrandViewSet(viewsets.ModelViewSet):
    queryset = ProductBrand.objects.all()
    serializer_class = ProductBrandSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer