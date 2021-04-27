from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler

import stripe

#Note that the code for webhook in Stripe is no longer on their page.
#So this is a borrowed version from lesson
#(I renamed the wh_secret to endpoint_secret).

@require_POST
@csrf_exempt
def webhook(request):
    """This calls out webhooks from stripe"""
    #Stripe call creation

    endpoint_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    #Obtain the webhook data and confirm the signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    
    # This creates up a webhook handler
    handler = StripeWH_Handler(request)

    # This calls up a dictionary list from webhook events
    event_map = {
        'payment_intent.succeeded': handler.webhook_payment_successful,
        'payment_intent.payment_failed': handler.webhook_payment_failed,
    }

    # Obtains a webhook type from Stripe
    event_type = event['type']

    event_handler = event_map.get(event_type, handler.webhook_event)

    # This calls up the event of the handler
    response = event_handler(event)
    return response
