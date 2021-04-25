from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('purchase_success/<order_number>', views.purchase_success, name='purchase_success'),
]
