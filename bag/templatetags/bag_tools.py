from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Custom template filter to calculate the
    subtotal for a product.
    """
    return price * quantity
