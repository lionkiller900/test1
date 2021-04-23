from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_pack(request):
    return render(request, 'pack/pack.html')

def put_to_bag(request, item_id):

    product = Product.objects.get(id=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    pack = request.session.get('pack', {})

    if size:
        if item_id in list(pack.keys()):
            if size in pack[item_id]['items_by_size'].keys():
                pack[item_id]['items_by_size'][size] += quantity
            else:
                pack[item_id]['items_by_size'][size] = quantity
        else:
            pack[item_id] = {'items_by_size': {size: quantity}}

    else:
        if item_id in list(pack.keys()):
            pack[item_id] += quantity
        else:
            pack[item_id] = quantity
            messages.success(request, f'Placed {product.name} to your pack')

    request.session['pack'] = pack
    return redirect(redirect_url)


def edit_pack(request, item_id):
    product = get_object_or_404(Product, name=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    pack = request.session.get('pack', {})

    if size:
        if quantity > 0:
            pack[item_id]['items_by_size'][size] = quantity
        else:
            del pack[item_id]['items_by_size'][size]
            if not pack[item_id]['items_by_size']:
                pack.pop(item_id)
    else:
        if quantity > 0:
            pack[item_id] = quantity
        else:
            pack.pop(item_id)

    request.session['pack'] = pack
    return redirect(reverse('view_pack'))


def delete_pack(request, item_id):
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        pack = request.session.get('pack', {})

        if size:
                del pack[item_id]['items_by_size'][size]
                if not pack[item_id]['items_by_size']:
                    pack.pop(item_id)
        else:
            pack.pop(item_id)

        request.session['pack'] = pack
        return HttpResponse(status=200)
    except Exception as exe:
        return HttpResponse(status=500)