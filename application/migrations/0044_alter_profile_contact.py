# Generated by Django 4.2.3 on 2023-08-14 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0043_rename_number_profile_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.BigIntegerField(null=True),
        ),
    ]
