# Generated by Django 5.0.6 on 2025-04-14 09:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_adminuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminuser',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
