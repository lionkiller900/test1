from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

# Views are created here.


def all_products(request):

    """This is for sorting and searching products online"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direct = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'less_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category_name'

            if 'direct' in request.GET:
                direct = request.GET['direct']
                if direct == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(categories__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'que' in request.GET:
            query = request.GET['que']
            if not query:
                messages.error(request, "The search has not been entered.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | \
                Q(descriptions__icontains=query)
            products = products.filter(queries)

    price_sorting = f'{sort}_{direct}'

    context = {
        'products': products,
        'seek_term': query,
        'present_categories': categories,
        'price_sorting': price_sorting,
    }

    return render(request, 'products/products.html', context)


def product_description(request, product_id):
    """This is for viewing the product description"""

    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product,
    }

    return render(
        request, 'products/product_description.html',
        context
        )


@login_required
def put_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Only account holders are allowed.')
        return redirect(reverse('frontpage'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Shoe product is now added!')
            return redirect(reverse('product_description', args=[product.id]))
        else:
            messages.error(request, 'There is a problem. \
                                    Please make sure it is done correctly.')
    else:
        form = ProductForm()

    template = 'products/put_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only account holders are allowed.')
        return redirect(reverse('frontpage'))

    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success! It is now updated')
            return redirect(reverse('product_description', args=[product_id]))
        else:
            messages.error(
                request, 'Could not update the shoe. \
                Ensure that it is done correctly.'
                )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Updating {product.name}')

    template = 'products/update_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only account holders are allowed.')
        return redirect(reverse('frontpage'))
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'This has now been deleted')
    return redirect(reverse('products'))
