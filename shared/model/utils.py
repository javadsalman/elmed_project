from django.utils.text import slugify
from django.utils.html import format_html

def get_slug(slug):
    return slugify(slug.lower().translate(str.maketrans('üöğəçşı', 'uogecsi')))

from django.utils.safestring import mark_safe

def get_image_tag(url):
    return mark_safe(format_html(u'<img src="{}" width="200" style="background-color: white"/>', url))

def get_slug_link(slug, get_absolute_url):
    if slug:
        return mark_safe(format_html('<a href="{0}">{1}{0}</a>', get_absolute_url(), 'www.elmed.az'))
    return '-'

from bs4 import BeautifulSoup
from bs4.element import Comment

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body, length=190):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    result = u" ".join(t.strip() for t in visible_texts)
    return result if len(result) <= length else result[:length] + '...'