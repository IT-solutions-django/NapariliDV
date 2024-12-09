from django import template
import locale


register = template.Library()


@register.filter(name='price_format')
def price_format(value: str):
    try:
        value = int(value)
        return f"{value:,}".replace(',', ' ')
    except (ValueError, TypeError):
        return value
