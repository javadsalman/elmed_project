from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'pages/home/home.html'
    

class AboutView(TemplateView):
    template_name = 'pages/about/about.html'
    
    
class ContactView(TemplateView):
    template_name = 'pages/contact/contact.html'
