from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    
    readonly_fields = ('product_number', 'date', 
                    'cost_of_order', 'overall_cost', 
                    'grand_cost')

    fields = ('product_number', 'date', 'Name', 'email', 
            'phone_number', 'home_Address', 'home_Address_continued', 
            'postcode', 'county', 'country')

    list_display = ('product_number', 'date', 'Name', 
    'overall_cost', 'cost_of_order', 
    'grand_cost')

    ordering = ('-date',)

admin. site.register(Order, OrderAdmin)