from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time

class StripeWH_Handler:

    def __init__(self, request):
        self.request = request
    """This deals with Webhooks anytime it is being called"""

    def _send_email_details(self, order):
        """This send the customer the confirmation email"""
        customer_email = order.email
        email_subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order':order})
        email_body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order':order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def webhook_event(self, event):
        """This deals with Webhook event that comes unknowingly"""
        
        return HttpResponse(
            content=f'Unhandled webhook obtained: {event["type"]}',
            status=200)


    def webhook_payment_successful(self, event):
        """This deals with payment_intent.succeeded from Stripe"""
        
        intent = event.data.object
        p_id = intent.id
        pack = intent.metadata.pack
        save_detail = intent.metadata.save_detail
        
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_cost = round(intent.charges.data[0].amount / 100, 2)
        
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_detail:
                profile.default_phone_number = shipping_details.phone,
                profile.default_home_Address = shipping_details.address.line1,
                profile.default_home_Address_continued = shipping_details.address.line2,
                profile.default_postcode = shipping_details.address.postal_code,
                profile.default_county = shipping_details.address.city,
                profile.default_country = shipping_details.address.country,
                profile.save()
        
        order_present = False
        seek = 1
        while seek <= 6:
            try:
                order = Order.objects.get(
                    Name__iexact=shipping_details.name,
                    user_account=profile,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    home_Address__iexact=shipping_details.address.line1,
                    home_Address_continued__iexact=shipping_details.address.line2,
                    postcode__iexact=shipping_details.address.postal_code,
                    county__iexact=shipping_details.address.city,
                    country__iexact=shipping_details.address.country,
                    grand_cost=grand_cost,
                    original_pack=pack,
                    stripe_p_id=p_id,
                )
                order_present = True
                break
            except Order.DoesNotExist:
                seek +=1
                time.sleep(1)
        if order_present:
            self._send_email_details(order)
            return HttpResponse(
                content=f'Webhook obtained: {event["type"]} | Good news. This is now in the database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    Name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    home_Address=shipping_details.address.line1,
                    home_Address_continued=shipping_details.address.line2,
                    postcode=shipping_details.address.postal_code,
                    county=shipping_details.address.city,
                    country=shipping_details.address.country,
                    original_pack=pack,
                    stripe_p_id=p_id,
                )
                for item_id, item_data in json.load(pack).items():
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook obtained: {event["type"]} | There is an error: {e}',
                    status=500)
        self._send_email_details(order)
        return HttpResponse(
            content=f'Webhook obtained: {event["type"]} | Goodnews: webhook order created',
            status=200)

    def webhook_payment_failed(self, event):
        """This deals with payment_intent.failed"""
        
        return HttpResponse(
            content=f'Webhook obtained: {event["type"]}',
            status=200)