# Generated by Django 3.0.4 on 2020-05-28 20:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Comm', '0026_auto_20200528_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 28, 20, 27, 12, 815513, tzinfo=utc)),
        ),
    ]
