# Generated by Django 4.2.3 on 2023-08-09 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_job_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='showcompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_image', models.ImageField(upload_to='img/')),
                ('address', models.CharField(max_length=200, null=True)),
                ('company_name', models.CharField(max_length=50)),
                ('developer', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=10)),
                ('languages', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.job')),
            ],
        ),
    ]
