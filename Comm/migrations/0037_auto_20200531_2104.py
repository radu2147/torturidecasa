# Generated by Django 3.0.4 on 2020-05-31 18:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Comm', '0036_auto_20200531_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 31, 18, 4, 23, 821164, tzinfo=utc)),
        ),
    ]
