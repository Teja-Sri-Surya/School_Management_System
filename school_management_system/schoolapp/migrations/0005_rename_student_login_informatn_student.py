# Generated by Django 3.2.25 on 2025-04-11 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0004_course_enrollment_instructor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student_login_informatn',
            new_name='Student',
        ),
    ]
