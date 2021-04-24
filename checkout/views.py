from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from pack.contexts import pack_contents

import stripe

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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