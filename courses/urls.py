from . import views
from django.urls import path, include
from rest_framework import routers
from .api import CourseViewSet

router = routers.DefaultRouter()
router.register('courses', CourseViewSet, 'courses')

urlpatterns = [
    path("courses", views.courses, name="courses"),
    path("update_course/<int:id>", views.update_course, name='update_course'),
    path("delete_course/<int:id>", views.delete_course, name="delete_course"),
    path("course_detail/<int:id>", views.course_detail, name="course_detail"),
    path('api/', include(router.urls)),
]