# Generated by Django 5.0.6 on 2025-04-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_teamtestimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurPartners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('image', models.FileField(default='team_images/Logo_IntelliSurge_TM_No_BG.png', upload_to='partner_logos/')),
            ],
        ),
    ]
