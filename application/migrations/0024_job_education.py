# Generated by Django 4.2.3 on 2023-08-11 07:28

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0023_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='education',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
