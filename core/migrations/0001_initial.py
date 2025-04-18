# Generated by Django 5.0.6 on 2025-04-11 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(blank=True)),
                ('content', models.TextField()),
                ('image_url', models.URLField(blank=True)),
                ('youtube_url', models.URLField(blank=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('job_type', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Internship', 'Internship'), ('Contract', 'Contract'), ('Remote', 'Remote')], max_length=50)),
                ('salary_range', models.CharField(blank=True, max_length=100, null=True)),
                ('job_description', models.TextField()),
                ('requirements_qualifications', models.TextField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('apply_link', models.URLField()),
            ],
        ),
    ]
