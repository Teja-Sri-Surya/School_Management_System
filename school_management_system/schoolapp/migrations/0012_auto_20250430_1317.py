# Generated by Django 3.2.25 on 2025-04-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0011_auto_20250426_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='total_seats',
            field=models.IntegerField(default=30),
        ),
    ]
