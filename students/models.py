from django.db import models
from courses.models import Course

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    status = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'
    