from django import template

register = template.Library()


@register.filter()
def upper_name(value, **kwargs):
    return value.upper()
