# Generated by Django 3.0.4 on 2020-06-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personalize', '0006_auto_20200622_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='customorder',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
