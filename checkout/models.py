import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

class Order(models.Model):
    product_number = models.CharField(max_length=40, null=False, blank=False)
    Name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=300, null=False, blank=False)
    phone_number = models.CharField(max_length=60, null=False, blank=False)
    home_Address = models.CharField(max_length=60, null=False, blank=False)
    home_Address_continued = models.CharField(max_length=60, null=False, blank=False)
    postcode = models.CharField(max_length=30, null=False, blank=False)
    county = models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    cost_of_order = models.DecimalField(max_digits=8, decimal_places = 2, null=False, blank=False)
    overall_cost = models.DecimalField(max_digits=10, decimal_places = 2, null=False, blank=False)
    grand_cost = models.DecimalField(max_digits=10, decimal_places = 2, null=False, blank=False)

    def _generate_order_number(self):

        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.overall_cost = self.lineitems.aggregate(Sum('lineitems_overall'))['lineitem_overall__sum'] or 0
        if self.overall_cost < settings.FREE_DELIVERY_LIMIT:
            self.cost_of_order = self.overall_cost * settings.STANDARD_DELIVERY_PERCENTAGE/100
        else:
            self.cost_of_order = 0
        self.grand_cost = self.overall_cost + self.cost_of_order
        self.save()

    def save(self, *args, **kwargs):

        if not self.product_number:
            self.product_number = self._generate_product_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='Lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=3, null=True, blank=True) 
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=8, decimal_places = 2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):

        self.lineitems_overall = self.product.prices * self.quantitys
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Skus {self.product.skus} on order {self.order.product_number}'
        
