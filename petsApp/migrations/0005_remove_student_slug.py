# Generated by Django 2.1.5 on 2024-03-21 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petsApp', '0004_student_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='slug',
        ),
    ]
