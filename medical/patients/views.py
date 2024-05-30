from django.shortcuts import render, redirect
from . forms import PatientForm
from . models import Patient
from django.contrib import messages

def patients(request):
    form = PatientForm(request.POST or None)
    patients = Patient.objects.all()
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Paciente creado correctamente.')
            return redirect('patients')    
        except:
            messages.error(request, 'No se puede crear el paciente.')
    return render(request, 'patients/index.html', {'form': form, 'patients': patients})