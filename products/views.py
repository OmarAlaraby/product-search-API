from rest_framework import viewsets
from .models import Product, ProductBrand, ProductCategory
from .serializers import ProductSerializer, ProductBrandSerializer, ProductCategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter

# utils
from django.db.models import Q
from functools import reduce
import operator
from decouple import config
import deepl
from .utils import correct_spelling

# caching 
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

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
            translated = translator.translate_text(keyword, target_lang="EN-US").text

            print(keyword, translated)
            print(translated, correct_spelling(translated))
            
            candidates = correct_spelling(translated)
            # print(candidates)
            search_fields = [
                "name", "description", "brand__name", "category__name",
                "ingredients", "allergens"
            ]

            queries = []
            for candidate in candidates:
                for field in search_fields:
                    queries.append(Q(**{f"{field}__icontains": candidate}))

            combined_query = reduce(operator.or_, queries)
            queryset = queryset.filter(combined_query).distinct()

        return queryset
    
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'search', openapi.IN_QUERY,
                description="Search across product fields (with translation and spelling correction)",
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
    @method_decorator(cache_page(int(config('CACHING_TIMEOUT'))))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(int(config('CACHING_TIMEOUT'))))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class ProductBrandViewSet(viewsets.ModelViewSet):
    queryset = ProductBrand.objects.all()
    serializer_class = ProductBrandSerializer
    
    @method_decorator(cache_page(int(config('CACHING_TIMEOUT'))))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @method_decorator(cache_page(int(config('CACHING_TIMEOUT'))))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    
    @method_decorator(cache_page(int(config('CACHING_TIMEOUT'))))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @method_decorator(cache_page(int(config('CACHING_TIMEOUT'))))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)