from django import template
import locale


register = template.Library()


@register.filter(name='price_format')
def price_format(value: str):
    try:
        value = int(value)
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        return locale.format_string("%d", value, grouping=True).replace(',', ' ')
    except (ValueError, TypeError):
        return value
