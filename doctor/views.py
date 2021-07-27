from django.shortcuts import render

# Create your views here.
def doctors(request):
    return render(request, 'doctor/doctor_list/doctor_list.html')

def doctor_detail(request):
    return render(request, 'doctor/doctor_detail/doctor_detail.html')