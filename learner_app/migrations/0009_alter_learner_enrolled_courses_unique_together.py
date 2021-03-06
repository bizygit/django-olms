# Generated by Django 3.2.9 on 2022-01-11 12:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learner_app', '0008_alter_learner_enrolled_courses_learner_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='learner_enrolled_courses',
            unique_together={('learner_id', 'course_id')},
        ),
    ]
