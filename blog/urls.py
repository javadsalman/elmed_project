from django.urls import path
from blog.views import article, ArticleList, ArticleDeatil

urlpatterns = [
    path('', ArticleList.as_view(), name='blog'),
    path('<int:pk>/<str:slug>/', ArticleDeatil.as_view(), name='article')
]
