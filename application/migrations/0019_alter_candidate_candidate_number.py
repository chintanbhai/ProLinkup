# Generated by Django 4.2.3 on 2023-08-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0018_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='candidate_number',
            field=models.IntegerField(max_length=10),
        ),
    ]
