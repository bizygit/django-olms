# Generated by Django 3.2.9 on 2022-01-11 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learner_app', '0006_auto_20220111_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learner_enrolled_courses',
            name='lecture_id',
        ),
        migrations.RemoveField(
            model_name='lecture_classes',
            name='lecture_id',
        ),
    ]