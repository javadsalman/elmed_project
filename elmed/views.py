from django.shortcuts import render
from django.views.generic import TemplateView
from doctor.models import Doctor
from blog.models import Article
from departament.models import Departament
    

class AboutView(TemplateView):
    template_name = 'pages/about/about.html'
    
    
class ContactView(TemplateView):
    template_name = 'pages/contact/contact.html'

def home(request):
    doctors = Doctor.objects.all().order_by('?')[:5]
    departaments = Departament.objects.all()
    articles = Article.objects.all()[:3]
    return render(request, 'pages/home/home.html', {
        'doctors': doctors,
        'departaments': departaments,
        'articles': articles
    })