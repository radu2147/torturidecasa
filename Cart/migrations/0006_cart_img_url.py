# Generated by Django 3.0.4 on 2020-06-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0005_auto_20200518_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='img_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
