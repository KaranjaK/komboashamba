# Generated by Django 4.1.4 on 2022-12-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_profile_bio_remove_profile_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]