from django.db import models
from courses.models import Course
from students.models import Student

# Create your models here.
class Registration(models.Model):
    course = models.ManyToManyField(Course)
    student = models.ManyToManyField(Student)
    
    def __str__(self) -> str:
        return f'Registration'