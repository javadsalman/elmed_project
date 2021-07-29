from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.html import format_html

def get_slug(slug):
    return slugify(slug.lower().translate(str.maketrans('üöğəçş', 'uogecs')))

def get_image_tag(url):
    return mark_safe(format_html(u'<img src="{}" width="200" style="background-color: white"/>', url))

def get_slug_link(slug, get_absolute_url):
    if slug:
        return mark_safe(format_html('<a href="{0}">{1}{0}</a>', get_absolute_url(), 'www.elmed.az'))
    return '-'