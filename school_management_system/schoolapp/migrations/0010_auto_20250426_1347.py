# Generated by Django 3.2.25 on 2025-04-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0009_student_submit_assignment_pro_submitted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_courses_with_teacher_name',
            name='class_schedule',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student_courses_with_teacher_name',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
