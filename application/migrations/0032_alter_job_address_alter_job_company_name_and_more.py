# Generated by Django 4.2.3 on 2023-08-12 04:50

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0031_alter_job_address_alter_job_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='company_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='developer',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='education',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='languages',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='time',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='job',
            name='working_hours',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
