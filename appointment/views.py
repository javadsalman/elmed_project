from shared.general.date import next_weekday_date
from django.shortcuts import redirect, render
from appointment.forms import AppointmentForm
from doctor.models import Doctor
from departament.models import Departament

# Create your views here.
def appointment(request):
    if request.method == 'GET':
        doctor = request.GET.get('doctor')
        departament = request.GET.get('departament')
        date = request.GET.get('weekday') and next_weekday_date(int(request.GET['weekday']))
        return render(request, 'appointment/appointment/appointment.html', {
            'doctors': Doctor.objects.all(),
            'departaments': Departament.objects.all(),
            'selected_doctor': doctor,
            'selected_departament': departament,
            'selected_date': date,
        })
    elif request.method =='POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback', result='ugurlu')
        else:
            print(form.errors)
            return redirect('feedback', result='ugursuz')
            
            
def feedback(request, result):
    return render(request, 'appointment/feedback/feedback.html', {'success': result == 'ugurlu'})