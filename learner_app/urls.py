from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='learner_app/index.html'), name='Home'),
    path('add-course/', AddCourse.as_view(), name="addcourse"),
    path('enroll-course/', EnrollCourse, name="enrollcourse"),
    path('enrolled-courses/', EnrolledCourses.as_view(), name="enrolledcourses"),
    path('enroll-delete/<pk>/', EnrollDelete.as_view(), name="enrolldelete"),
    path('list-course/', ListCourse.as_view(), name="listcourse"),
    path('learner-enrolled-course/', LearnerEnrolledCourse.as_view(), name="learnerenrolledcourse"),
    path('listcourse-delete/<pk>/', ListcourseDelete.as_view(), name="listcoursedelete"),
    path('enrolled-course-delete/<pk>/', EnrolledCourseDelete.as_view(), name="enrolledcoursedelete"),

]+ static(settings.MEDIA_URL, 
            document_root=settings.MEDIA_ROOT)

