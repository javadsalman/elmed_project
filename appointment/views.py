from django.shortcuts import redirect, render
from appointment.forms import AppointmentForm
from doctor.models import Doctor
from departament.models import Departament

# Create your views here.
def appointment(request):
    if request.method == 'GET':
        print('\n\n\n\n', request.GET.get('departament'), '\n\n\n')
        return render(request, 'appointment/appointment/appointment.html', {
            'doctors': Doctor.objects.all(),
            'departaments': Departament.objects.all(),
            'selected_doctor': request.GET.get('doctor'),
            'selected_departament': request.GET.get('departament')
        })
    elif request.method =='POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback', result='ugurlu')
        else:
            return redirect('feedback', result='ugursuz')
            
            
def feedback(request, result):
    return render(request, 'appointment/feedback/feedback.html', {'success': result == 'ugurlu'})