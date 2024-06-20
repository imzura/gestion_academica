from . import views
from django.urls import path

urlpatterns = [
    path("", views.students, name="students"),
    path("update_student/<int:id>", views.update_student, name="update_student"),
    path("delete_student/<int:id>", views.delete_student, name="delete_student"),
    path("student_detail/<int:id>", views.student_detail, name="student_detail"),
]