from django import forms
from .models import Course
from students.models import Student

class CourseForm(forms.ModelForm):
    student = forms.ModelMultipleChoiceField(
        queryset=Student.objects.filter(status=True),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'students'}),
        label='Estudiantes'
    )

    class Meta:
        model = Course
        fields = ['name', 'description', 'start_date', 'ending_date', 'student', 'status']
        labels = {
            'name': 'Nombre del curso',
            'description': 'Descripción',
            'start_date': 'Fecha de inicio',
            'ending_date': 'Fecha de fin',
            'status': 'Estado'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre del curso',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Ingrese una descripción',
                'class': 'form-control'
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'ending_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'status': forms.HiddenInput()
        }