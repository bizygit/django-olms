# Generated by Django 3.2.9 on 2022-01-11 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learner_app', '0003_learner_enrolled_courses_learner_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture_classes',
            name='course_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
