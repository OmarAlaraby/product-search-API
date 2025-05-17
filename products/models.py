from django.db import models


class ProductBrand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    serving_size = models.CharField(max_length=100, blank=True, null=True)
    servings_per_container = models.FloatField(blank=True, null=True)
    calories = models.FloatField(blank=True, null=True)
    total_fat = models.FloatField(blank=True, null=True)
    saturated_fat = models.FloatField(blank=True, null=True)
    trans_fat = models.FloatField(blank=True, null=True)
    cholesterol = models.FloatField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True)
    total_carbohydrates = models.FloatField(blank=True, null=True)
    dietary_fiber = models.FloatField(blank=True, null=True)
    sugars = models.FloatField(blank=True, null=True)
    added_sugars = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    vitamin_d = models.FloatField(blank=True, null=True)
    calcium = models.FloatField(blank=True, null=True)
    iron = models.FloatField(blank=True, null=True)
    potassium = models.FloatField(blank=True, null=True)

    ingredients = models.TextField(blank=True, null=True)
    allergens = models.TextField(blank=True, null=True)

    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_organic = models.BooleanField(default=False)

    def __str__(self):
        return self.name