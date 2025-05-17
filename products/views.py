from rest_framework import viewsets
from .models import Product, ProductBrand, ProductCategory
from .serializers import ProductSerializer, ProductBrandSerializer, ProductCategorySerializer

# utils
from django.db.models import Q
from decouple import config
import deepl
from functools import reduce
import operator
from langdetect import detect

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
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


class ProductBrandViewSet(viewsets.ModelViewSet):
    queryset = ProductBrand.objects.all()
    serializer_class = ProductBrandSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer