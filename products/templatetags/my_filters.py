from django import template

register = template.Library()

@register.filter
def to_list(value, arg=None):
    if value is None:
        value = 0
    if arg:
        return range(value, arg + 1)
    return range(1, value + 1)