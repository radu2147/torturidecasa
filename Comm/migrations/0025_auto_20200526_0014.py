# Generated by Django 3.0.4 on 2020-05-25 21:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Comm', '0024_auto_20200526_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 25, 21, 14, 49, 470535, tzinfo=utc)),
        ),
    ]
