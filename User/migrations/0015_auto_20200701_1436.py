# Generated by Django 3.0.4 on 2020-07-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_auto_20200625_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
