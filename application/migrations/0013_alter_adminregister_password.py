# Generated by Django 4.2.3 on 2023-08-09 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_adminregister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminregister',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]