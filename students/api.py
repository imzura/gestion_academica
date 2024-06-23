from .models import Student
from rest_framework import permissions, viewsets
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permissions_classes = [permissions.IsAuthenticated]