from django.views.generic import ListView, DetailView
from departament.models import Departament
from doctor.models import Doctor

# Create your views here.
class DepartamentDetail(DetailView):
    template_name = 'departament/departament_detail/departament_detail.html'
    model = Departament
    context_object_name = 'departament'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Departament.objects.all().exclude(id=context['departament'].id)
        context["departaments"] = Departament.objects.all()
        context["doctors"] = Doctor.objects.all()
        return context
    
    

class DepartamentList(ListView):
    model = Departament
    template_name = 'departament/departament_list/departament_list.html'
    context_object_name = 'departaments'