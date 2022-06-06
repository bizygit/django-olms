from django import forms
from django.contrib.auth.models import User
from .models import Lecture_Classes, Learner_Enrolled_Courses
from accounts.models import Profile

# def sample_view(request):
#     current_user = request.user
#     return current_user.id

class AddLectureClasses(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AddLectureClasses, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     self.fields['lecture_id'].widget.attrs['readonly'] = True
    # x = sample_view()
    # lecture_id = forms.CharField(widget=forms.HiddenInput(), initial=x)

    class Meta:
        model=Lecture_Classes
        # widgets = {'lecture_id': forms.HiddenInput()}
        # fields='__all__'
        fields=('course_name',)


class LearnerEnrolledCourses(forms.ModelForm):

    # lecture_id = forms.ModelChoiceField(queryset=User.objects.filter(role = 'lecture'))
    # lecture_id = forms.ModelChoiceField(queryset=Profile.objects.filter(role = 'lecture').values_list('user_id', flat=True))

    class Meta:
        model=Learner_Enrolled_Courses
        widgets = {'learner_id': forms.HiddenInput()}
        # fields='__all__'
        fields=('learner_id', 'course_id')