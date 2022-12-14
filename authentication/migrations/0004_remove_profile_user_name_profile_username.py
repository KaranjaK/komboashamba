# Generated by Django 4.1.4 on 2022-12-14 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_profile_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
