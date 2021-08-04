from shared.general.date import next_weekday_date
from django.shortcuts import redirect, render
from appointment.forms import AppointmentForm
from doctor.models import Doctor
from departament.models import Departament
from appointment.utils import check_recatpcha

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
        recatpcha_data = request.POST.get("g-recaptcha-response")
        rec_result = check_recatpcha(recatpcha_data)
        form = AppointmentForm(request.POST)
        # print(f'\n\n\n{rec_result}\n\n\n')
        # print(f'\n\n\n{form.errors}\n\n\n')
        if form.is_valid() and rec_result['success'] and rec_result['score'] > 0.7:
            form.save()
            return redirect('feedback', result='ugurlu')
        else:
            print(form.errors)
            return redirect('feedback', result='ugursuz')
            
            
def feedback(request, result):
    return render(request, 'appointment/feedback/feedback.html', {'success': result == 'ugurlu'})