from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """This is for sorting and searching products online"""

    products = Product.objects.all()

    context = {
        'products': products, 
    }

    return render(request, 'products/products.html', context)

def product_description(request, product_id):
    """This is for viewing the product description"""

    products = get_object_or_404(Product, id=product_id)

    context = {
        'products': products, 
    }

    return render(request, 'products/product_description.html', context)