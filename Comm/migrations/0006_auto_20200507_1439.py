# Generated by Django 3.0.4 on 2020-05-07 11:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Comm', '0005_auto_20200503_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 7, 11, 39, 20, 882880, tzinfo=utc)),
        ),
    ]