from django.conf.urls.i18n import urlpatterns
from django.urls import path
from blog.views import blog

urlpatterns = [
    path('', blog, name='blog')
]
