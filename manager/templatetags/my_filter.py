from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def my_decimal(number, decimal_places=2, decimal=','):
    result = intcomma(number)
    result += decimal if decimal not in result else ''
    while len(result.split(decimal)[1]) != decimal_places:
        result += '0'
    return result

