from django import template


register = template.Library()


@register.filter(name='float_dot_format')
def float_dot_format(value: float):
    try:
        return str(value).replace(',', '.')
    except (ValueError, TypeError):
        return value
