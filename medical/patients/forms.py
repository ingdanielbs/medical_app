from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['status']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'document': 'Documento',
            'address': 'Dirección',
            'email': 'Correo Electrónico',
            'phone': 'Teléfono',
            'date_of_birth': 'Fecha de Nacimiento',           
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={                    
                    'placeholder': 'Ingrese el nombre del paciente',                    
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese los apellidos del paciente',                    
                }
            ),
            'document': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el documento del paciente',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese la dirección del paciente',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'type': 'email',
                    'placeholder': 'Ingrese el correo electrónico del paciente',                    
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el teléfono del paciente',
                }
            ),
            'date_of_birth': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type': 'date',
                    'placeholder': 'Ingrese la fecha de nacimiento del paciente',
                }
            )
        }