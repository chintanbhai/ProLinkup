# Generated by Django 4.2.3 on 2023-08-12 06:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0035_profile_apply_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='apply_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
