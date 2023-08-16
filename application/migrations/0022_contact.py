# Generated by Django 4.2.3 on 2023-08-10 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0021_alter_candidate_candidate_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=40)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]