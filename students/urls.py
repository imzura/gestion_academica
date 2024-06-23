from . import views
from django.urls import path, include
from rest_framework import routers
from .api import StudentViewSet

router = routers.DefaultRouter()
router.register('students', StudentViewSet, 'students')

urlpatterns = [
    path("students", views.students, name="students"),
    path("update_student/<int:id>", views.update_student, name="update_student"),
    path("delete_student/<int:id>", views.delete_student, name="delete_student"),
    path("student_detail/<int:id>", views.student_detail, name="student_detail"),
    path('api/', include(router.urls)),
]