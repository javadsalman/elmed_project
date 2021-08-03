from django.template import Library

register = Library()

@register.filter(name='adress_split')
def adress_split(adress, *args):
    return adress.split(',')