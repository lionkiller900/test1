from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItem(admin.ModelAdmin):
    readonly_fields = ('product_number', 'date', 
                    'cost_of_order', 'overall_cost', 
                    'grand_cost')

    fields = ('product_number', 'date', 'Name', 'email', 
            'phone_number', 'home_Address', 'home_Address_continued', 
            'postcode', 'county', 'country')
