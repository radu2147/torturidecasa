# Generated by Django 3.0.4 on 2020-09-25 16:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Personalize', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customorder',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
