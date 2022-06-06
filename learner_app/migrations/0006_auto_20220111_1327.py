# Generated by Django 3.2.9 on 2022-01-11 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learner_app', '0005_alter_learner_enrolled_courses_learner_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learner_enrolled_courses',
            name='lecture_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lecture_classes',
            name='lecture_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
