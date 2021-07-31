from django.template import Library
from urllib.parse import urlencode

register = Library()

@register.simple_tag
def edit_query(request, **kwargs):
    query = request.GET.copy()
    query.update(kwargs)
    return '?' + urlencode(query)
