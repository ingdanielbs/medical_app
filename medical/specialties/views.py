from django.shortcuts import render, redirect
from . forms import SpecialtyForm
from django.contrib import messages
from specialties.models import Specialty

# Create your views here.
def specialties(request):
    form = SpecialtyForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Especialidad creada correctamente.')
            return redirect('specialties')    
        except:
            messages.error(request, 'No se puede crear la especialidad.')
    return render(request, "specialties/index.html", {'form': form})

def edit_specialty(request, id):
    specialty = Specialty.objects.get(id=id)
    form = SpecialtyForm(request.POST or None, instance=specialty)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Especialidad actualizada correctamente.')
            return redirect('specialties')    
        except:
            messages.error(request, 'No se puede actualizar la especialidad.')
    return render(request, "specialties/edit.html", {'form': form})

