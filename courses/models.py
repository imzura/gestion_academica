from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    ending_date = models.DateField()
    status = models.BooleanField(default=True)
    student = models.ManyToManyField('students.Student')
    
    def __str__(self) -> str:
        return self.name

