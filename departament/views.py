from django.shortcuts import render
from django.views.generic import ListView
from departament.models import Departament

# Create your views here.
def depertament_detail(request, slug):
    return render(request, 'departament/departament_detail/departament_detail.html')

class DepartamentList(ListView):
    model = Departament
    template_name = 'departament/departament_list/departament_list.html'
    context_object_name = 'departaments'