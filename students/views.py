from django.shortcuts import render, redirect, get_object_or_404
from . forms import StudentForm
from django.contrib import messages
from students.models import Student

# Create your views here.
def students(request):
    form = StudentForm(request.POST or None)
    students = Student.objects.all()
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Estudiante registrado con éxito.')
            return redirect('students')
        except:
            messages.error(request, 'Ocurrió un error al registrar al estudiante.')
            return redirect('students')
    return render(request, "students/index.html", {'form':form, 'students':students })

def student_detail(request, id):
    students = Student.objects.get(id=id)
    return render(request, "students/student_detail.html", {'students': students})

def update_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Información actualizada con éxito.')
            return redirect('students')
        except:
            messages.error(request, 'Ocurrió un error al actualizar la información.')
            return redirect('students')
    return render(request, 'students/update_student.html', {'form': form})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    try:
        student.delete()
        messages.success(request, 'Estudiante eliminado con éxito.')
        return redirect('students')
    except:
        messages.error(request, 'Ocurrió un error al eliminar al estudiante.')
        return redirect('students')