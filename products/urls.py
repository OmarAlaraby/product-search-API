from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'brands', views.ProductBrandViewSet, basename='productbrand')
router.register(r'categories', views.ProductCategoryViewSet, basename='productcategory')

urlpatterns = [] + router.urls