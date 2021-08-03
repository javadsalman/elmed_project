from doctor.filters import DoctorFilter
from shared.pagination.pagination import get_page_list
from django.shortcuts import render
from django.views.generic import DetailView
from doctor.models import Doctor
from departament.models import Departament
from django_filters.views import FilterView
from doctor.filters import DoctorFilter

# Create your views here.
class DoctorDetail(DetailView):
    template_name = 'doctor/doctor_detail/doctor_detail.html'
    context_object_name = 'doctor'
    model = Doctor

class DoctorList(FilterView):
    template_name = 'doctor/doctor_list/doctor_list.html'
    context_object_name = 'doctors'
    paginate_by = 4
    filterset_class = DoctorFilter
    model = Doctor
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_list'] = get_page_list(context['page_obj'].number, context['page_obj'].paginator.num_pages, self.paginate_by)
        context['departaments'] = Departament.objects.all()
        return context
        
        