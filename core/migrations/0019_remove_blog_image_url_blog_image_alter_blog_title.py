# Generated by Django 5.0.6 on 2025-04-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_ourpartners'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image_url',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='Blog_image/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
