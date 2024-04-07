from django import template


register=template.Library()

@register.filter(name='farsinum')
def farsinum(value):
    value = str(value)
    trans_table = value.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
    return value.translate(trans_table)