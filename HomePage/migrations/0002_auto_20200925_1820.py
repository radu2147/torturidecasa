# Generated by Django 3.0.4 on 2020-09-25 15:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produs',
            name='image',
        ),
        migrations.AddField(
            model_name='produs',
            name='cake_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='avatar'),
        ),
    ]