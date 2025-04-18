# Generated by Django 5.0.6 on 2025-04-11 05:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_jobnotification_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobnotification',
            name='job_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='Untitled Job', max_length=200),
        ),
    ]
