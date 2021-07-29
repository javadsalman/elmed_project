from django.conf.urls.i18n import urlpatterns
from django.urls import path
from blog.views import article, blog

urlpatterns = [
    path('', blog, name='blog'),
    path('<int:pk>/<str:slug>/', article, name='article')
]
