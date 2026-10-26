from decimal import Decimal
from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value):
    if value is None or value == '':
        return '$0.00'
    try:
        val = Decimal(str(value))
        return f"${val:,.2f}"
    except (ValueError, TypeError):
        return value

@register.filter(name='total_parts_cost')
def total_parts_cost(car):
    if not car:
        return '$0.00'

    total = sum(part.price for part in car.required_parts.all())
    return f"${total:,.2f}"

@register.filter(name='mask_vin')
def mask_vin(vin):
    if not vin or len(vin) < 10:
        return vin
    return f"{vin[:4]}...{vin[-4:]}"

@register.simple_tag
def restoration_status_badge(car):
    count = car.required_parts.count()
    if count == 0:
        return '<span class="badge bg-success">Ready / No Parts Needed</span>'
    elif count <= 2:
        return f'<span class="badge bg-info text-dark">Minor Restoration ({count} parts)</span>'
    else:
        return f'<span class="badge bg-warning text-dark">Major Restoration ({count} parts)</span>'