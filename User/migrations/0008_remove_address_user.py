# Generated by Django 3.0.4 on 2020-05-28 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_auto_20200528_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
    ]
