from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """This is for sorting and searching products online"""

    products = Product.objects.all()

    context = {
        'products': products, 
    }

    return render(request, 'products/products.html', context)