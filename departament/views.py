from django.shortcuts import render

# Create your views here.
def departaments(request):
    return render(request, 'departament/departament_list/departament_list.html')

def depertament_detail(request):
    return render(request, 'departament/departament_detail/departament_detail.html')