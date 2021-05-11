from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'purchase_success/<product_number>',
        views.purchase_success, name='purchase_success'
        ),
    path(
        'stripe_checkout_data/',
        views.stripe_checkout_data,
        name='stripe_checkout_data'
        ),
    path('wh/', webhook, name='webhook'),
]
