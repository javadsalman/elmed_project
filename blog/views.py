from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog/blog/blog.html')

def article(request, pk, slug):
    return render(request, 'blog/article/article.html')