from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'last_name', 'document', 'email', 'status']
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'document': 'Documento',
            'email': 'Correo electrónico',
            'status': 'Estado'
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del estudiante'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ingrese el apellido del estudiante'}),
            'document': forms.TextInput(attrs={'placeholder': 'Ingrese el documento del estudiante'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ingrese el correo electrónico del estudiante', 'type': 'email'}),
            'status': forms.HiddenInput()  # Ocultar el campo de estado por defecto
        }
