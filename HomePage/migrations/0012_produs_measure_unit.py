# Generated by Django 3.0.4 on 2020-07-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0011_auto_20200724_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='produs',
            name='measure_unit',
            field=models.CharField(default='kg', max_length=5),
        ),
    ]