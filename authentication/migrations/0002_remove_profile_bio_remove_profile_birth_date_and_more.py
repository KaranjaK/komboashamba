# Generated by Django 4.1.4 on 2022-12-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='id_number',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='password2',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
