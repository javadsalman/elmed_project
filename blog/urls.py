from django.conf.urls.i18n import urlpatterns
from django.urls import path
from blog.views import article, blog

urlpatterns = [
    path('', blog, name='blog'),
    path('article', article, name='article')
]
