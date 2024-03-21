# Generated by Django 2.1.5 on 2024-03-20 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': 'Cats',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=32)),
                ('lastName', models.CharField(max_length=32)),
                ('noOfcats', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='cats',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petsApp.Student'),
        ),
    ]