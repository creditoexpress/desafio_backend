from django import template

register = template.Library()


@register.filter
def formata_preco(val):
    return f'R$ {val:.2f}'. replace('.', ',')
