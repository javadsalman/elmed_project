from blog.filters import BlogFilter
from django.shortcuts import render
from django.views.generic import DetailView
from blog.models import Article, Category
from shared.pagination.pagination import get_page_list
from django.db.models import Count
from django_filters.views import FilterView

# Create your views here.
def blog(request):
    return render(request, 'blog/blog/blog.html')

def article(request, pk, slug):
    return render(request, 'blog/article/article.html')

class ArticleDeatil(DetailView):
    template_name = 'blog/article/article.html'
    model = Article
    

class ArticleList(FilterView):
    template_name = 'blog/blog/blog.html'
    context_object_name = 'articles'
    paginate_by = 6
    filterset_class = BlogFilter
    model = Article
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_list'] = get_page_list(context['page_obj'].number, context['page_obj'].paginator.num_pages, self.paginate_by)
        context['categories'] = Category.objects.all().annotate(article_nums=Count('article'))
        context['total_count'] = self.get_queryset().count()
        return context
    