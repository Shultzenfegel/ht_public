from django import template

register = template.Library()


@register.filter
def format_decimal(value, precision):
    '''Форматирует число'''

    return f'{value:,.{precision}f}'.replace(',', ' ')


@register.filter
def pluralize_number(value, wordsList):
    '''Склоняет числительные'''
    
    words = wordsList.split(',')
    words = words + ['' for _ in range(3 - len(words))]

    if (value != 11 and value % 10 == 1):
        return f'{value} {words[0]}'

    if (not 12 <= value <= 14 and 2 <= value % 10 <= 4):
        return f'{value} {words[1]}'

    return f'{value} {words[2]}'
