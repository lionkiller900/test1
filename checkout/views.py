from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    pack = request.session.get('pack', {})
    if not pack:
        messgae.error(request, "There are no shoes in the pack")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IjVq8ANSSchvNACG3NkbGzuany4sXEzPZfCjePzFKs81MYok5zuWpqQ1kMtWUAZaVjU0vnPW2BHKZXYCmzegGlR00N91LyfTn',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)