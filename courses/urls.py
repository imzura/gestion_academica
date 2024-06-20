from . import views
from django.urls import path

urlpatterns = [
    path("", views.courses, name="courses"),
    path("update_course/<int:id>", views.update_course, name='update_course'),
    path("delete_course/<int:id>", views.delete_course, name="delete_course"),
    path("course_detail/<int:id>", views.course_detail, name="course_detail"),
]