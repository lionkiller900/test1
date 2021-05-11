from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from pack.contexts import pack_contents

import stripe
import json


@require_POST
def stripe_checkout_data(request):
    try:
        p_id = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(p_id, metadata={
            'pack': json.dumps(request.session.get('pack', {})),
            'save_detail': request.POST.get('save_detail'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Apologies no payment has occured.\
            Please come back soon.')
        return HttpResponse(content=e, status=400)


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
            'home_Address_continued': request.POST.get(
                'home_Address_continued', False
                ),
            'country': request.POST['country'],

        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            print("Form valid")
            order = order_form.save(commit=False)
            p_id = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_p_id = p_id
            order.original_pack = json.dumps(pack)
            order.save()
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
                    messages.error(request, (
                        "This footware is not found in our storage. \
                                            Get back to us soon.")
                    )
                    order.delete()
                    return redirect(reverse('view_pack'))
            request.session['save_detail'] = 'save_detail' in request.POST
            return redirect(
                reverse('purchase_success', args=[order.product_number])
                )
        else:
            print("Form not valid")
            messages.error(request, 'Carefully check! \
                There is an error in your form.')
    else:
        pack = request.session.get('pack', {})
        if not pack:
            messages.error(request, "There are no shoes in the pack")
            return redirect(reverse('products'))

        current_pack = pack_contents(request)
        overall = current_pack['overall_total']
        stripe_overall = round(overall * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_overall,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'Name': profile.user.get_full_name(),
                    'phone_number': profile.default_phone_number,
                    'home_Address': profile.default_home_Address,
                    'home_Address_continued':
                        profile.default_home_Address_continued,
                    'county': profile.default_county,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                    order_form = OrderForm()
        else:
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

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # This puts the user's profile to the purchase order
        order.user_account = profile
        order.save()

        if save_detail:
            profile_account = {
                'default_phone_number': order.phone_number,
                'default_postcode': order.postcode,
                'default_home_Addres': order.home_Addres,
                'default_home_Address_continued': order.home_Address_continued,
                'default_county': order.county,
                'default_country': order.country,
            }
            customer_profile_form = UserProfileForm(
                profile_account, instance=profile
                )
            if customer_profile_form.is_valid():
                customer_profile_form.save()
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
