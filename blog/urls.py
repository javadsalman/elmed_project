from django.conf.urls.i18n import urlpatterns
from django.urls import path
from blog.views import article, ArticleList

urlpatterns = [
    path('', ArticleList.as_view(), name='blog'),
    path('<int:pk>/<str:slug>/', article, name='article')
]
