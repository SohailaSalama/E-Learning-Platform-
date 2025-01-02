# Generated by Django 5.1.4 on 2025-01-02 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]
