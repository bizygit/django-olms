from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lecture_Classes(models.Model):
    course_id = models.BigAutoField(primary_key=True)
    course_name  = models.CharField(max_length=50, unique=True)

    # lecture_id = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'{self.course_name}'


class Learner_Enrolled_Courses(models.Model):
    enrollment_id = models.BigAutoField(primary_key=True)
    # learner_id = models.IntegerField(default=None)
    learner_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # lecture_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Lecture_Classes, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('learner_id', 'course_id')

    def __str__(self) -> str:
        return f'{self.course_id}'


