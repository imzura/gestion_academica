from django.shortcuts import render, redirect
from . forms import CourseForm
from django.contrib import messages
from courses.models import Course

# Create your views here.
def courses(request):
    form = CourseForm(request.POST or None)
    courses = Course.objects.all()
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Curso registrado con éxito.')
            return redirect('courses')
        except:
            messages.error(request, 'Ocurrió un error al registrar el curso.')
            return redirect('courses')
    return render(request, "courses/index.html", {'form':form, 'courses': courses })


def course_detail(request, id):
    courses = Course.objects.get(id=id)
    return render(request, "courses/course_detail.html", {'courses': courses})

def update_course(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Información actualizada con éxito.')
            return redirect('courses')
        except:
            messages.error(request, 'Ocurrió un error al actualizar la información.')
            return redirect('courses')
    return render(request, 'courses/update_course.html', {'form': form})

def delete_course(request, id):
    course = Course.objects.get(id=id)
    try:
        course.delete()
        messages.success(request, 'Curso eliminado con éxito.')
        return redirect('courses')
    except:
        messages.error(request, 'Ocurrió un error al eliminar el curso.')
        return redirect('courses')
    
