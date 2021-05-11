from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def pack_contents(request):

    pack_items = []
    overall = 0
    products_count = 0
    pack = request.session.get('pack', {})

    for item_id, quantity in pack.items():
        product = get_object_or_404(Product, id=item_id)
        overall += quantity * product.prices
        products_count += quantity
        pack_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if overall < settings.FREE_DELIVERY_LIMIT:
        delivery = overall * \
            Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        real_delivery_alpha = settings.FREE_DELIVERY_LIMIT - overall
    else:
        delivery = 0
        real_delivery_alpha = 0

    overall_total = delivery + overall

    content = {
        'pack_items': pack_items,
        'overall': overall,
        'products_count': products_count,
        'delivery': delivery,
        'real_delivery_alpha': real_delivery_alpha,
        'free_delivery_limit': settings.FREE_DELIVERY_LIMIT,
        'overall_total': overall_total,
    }

    return content
