from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from pack.contexts import pack_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        pack = request.session.get('pack', {})

        form_data = {
            'Name': request.POST['Name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'home_Address': request.POST.get('home_Address', False),
            'home_Address_continued': request.POST.get('home_Address_continued', False),
            'country': request.POST['county'],

        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            print("Form valid")
            order = order_form.save()
            for item_id, item_data in pack.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request,(
                        "This footware is not found in our storage. Get back to us soon.")
                    )
                    order.delete()
                    return redirect(reverse('view_pack'))


            request.session['save_detail'] = 'save_detail' in request.POST
            return redirect(reverse('purchase_success', args=[order.product_number]))
        else:
            print("Form not valid")
            messages.error(request, 'Carefully check! \
                There is an error in your form.')
    else:
        pack = request.session.get('pack', {})
        if not pack:
            messgae.error(request, "There are no shoes in the pack")
            return redirect(reverse('products'))

        current_pack = pack_contents(request)
        overall = current_pack['overall_total']
        stripe_overall = round(overall * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_overall,
            currency=settings.STRIPE_CURRENCY,
        )
        print("Intent", intent)
        order_form = OrderForm()
    
    if not stripe_public_key:
        messages.warning(request, 'your Stripe public key is not found. \
            Did forget to add it in the your environment settings?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

def purchase_success(request, product_number):
    """
    This deals with successful shoe purchase
    """
    save_detail = request.session.get('save_detail')
    order = get_object_or_404(Order, product_number=product_number)
    messages.success(request, f'Item Succesfully purchased! \
        This is your order number: {product_number}. An email confirming \
        your purchase will be sent to you on {order.email}.')

    if 'pack' in request.session:
        del request.session['pack']

    template = 'checkout/purchase_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)