from django import template


register = template.Library()

@register.filter(name='calc_halftotal')
def calc_halftotal(prices, quantity):
    return prices * quantity
