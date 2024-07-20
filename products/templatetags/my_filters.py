from django import template

register = template.Library()


@register.filter
def to_list(value, arg=None):
    """
    Converts a given integer into a list of integers.
    If an argument is provided, it returns a list starting
    from the given value to the argument. If no argument is
    provided, it returns a list starting from 1 to the given value.
    """
    if arg:
        return range(value, arg + 1)
    return range(1, value + 1)
