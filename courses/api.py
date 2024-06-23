from .models import Course
from rest_framework import permissions, viewsets
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permissions_classes = [permissions.IsAuthenticated]