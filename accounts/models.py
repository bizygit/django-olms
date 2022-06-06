from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
'''
    In Django Authentication 
        we you want to add some extra fields 
        to our User model then we want to create a
        proxy Model in django.
        as follows.

        proxy model always implement a one to one 
        relationship with User Model.
'''
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # CH=(
    #     ('lecture','Lecture'),
    #     ('learner','Learner')
    # )
    # role = models.CharField(max_length=10,choices=CH,default='admin')

# below function is called automatically.

@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
