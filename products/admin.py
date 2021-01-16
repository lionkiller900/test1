from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    display_list = (
        'skus',
        'categories',
        'name',
        'description', 
        'image_url',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    display_list = (
        'name',
    )
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)