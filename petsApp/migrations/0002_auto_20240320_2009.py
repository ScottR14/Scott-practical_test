# Generated by Django 2.1.5 on 2024-03-20 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='lastName',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]