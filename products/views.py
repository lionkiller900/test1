from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    """This is for sorting and searching products online"""

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(categories__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'que' in request.GET:
            query = request.GET['que']
            if not query:
                messages.error(request, "The search has not been entered.")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(descriptions__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'seek_term': query,
        'present_categories': categories,
    }

    return render(request, 'products/products.html', context)

def product_description(request, product_id):
    """This is for viewing the product description"""

    products = get_object_or_404(Product, id=product_id)

    context = {
        'products': products, 
    }

    return render(request, 'products/product_description.html', context)