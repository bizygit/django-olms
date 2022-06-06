from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import AddLectureClasses, LearnerEnrolledCourses
from learner_app.models import Lecture_Classes, Learner_Enrolled_Courses

from .models import Lecture_Classes

class AddCourse(LoginRequiredMixin, CreateView):
    form_class= AddLectureClasses
    template_name="learner_app/add_course.html"
    success_url=reverse_lazy('listcourse')
    redirect_field_name = 'login'

# @login_required(login_url='login')
# def AddCourse(req):
#     form = AddLectureClasses(req.POST)
#     if req.method=='POST':
#         if form.is_valid():
#             form.save()
#             messages.success(req, 'Course Added Successfully....')
#             return redirect('addcourse')
#     else:
#         # form = AddLectureClasses(initial={'lecture_id': req.user})
#         data ={'form':form}
#         return render(req, 'learner_app/add_course.html', data)

# class EnrollCourse(LoginRequiredMixin, CreateView):
#     form_class= LearnerEnrolledCourses
#     template_name="learner_app/enroll_course.html"
#     success_url=reverse_lazy('enrollcourse')
#     redirect_field_name = 'login'


@login_required(login_url='login')
def EnrollCourse(req):
    if req.method=='POST':
        form = LearnerEnrolledCourses(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Course Enrolled Successfully....')
            return redirect('enrolledcourses')
        else:
            form = LearnerEnrolledCourses(initial={'learner_id': req.user.id})
            data ={'form':form}
            messages.warning(req, 'Already enrolled for the specific course...')
            return render(req, 'learner_app/enroll_course.html', data)
    else:
        form = LearnerEnrolledCourses(initial={'learner_id': req.user.id})
        data ={'form':form}
        return render(req, 'learner_app/enroll_course.html', data)

class EnrolledCourses(ListView):
    model = Learner_Enrolled_Courses
    context_object_name = 'enrolledcourses'
    template_name='learner_app/enrolled_courses.html'


class EnrollDelete(DeleteView):
    model=Learner_Enrolled_Courses
    success_url=reverse_lazy('enrolledcourses')


class ListCourse(ListView):
    model = Lecture_Classes
    context_object_name = 'listcourse'
    template_name='learner_app/listcourse.html'

class LearnerEnrolledCourse(ListView):
    model = Learner_Enrolled_Courses
    context_object_name = 'learnerenrolledcourse'
    template_name='learner_app/learnerenrolledcourse.html'


class ListcourseDelete(DeleteView):
    model=Lecture_Classes
    success_url=reverse_lazy('listcourse')


class EnrolledCourseDelete(DeleteView):
    model=Learner_Enrolled_Courses
    success_url=reverse_lazy('learnerenrolledcourse')
