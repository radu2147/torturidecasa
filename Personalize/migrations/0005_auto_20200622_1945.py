# Generated by Django 3.0.4 on 2020-06-22 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personalize', '0004_auto_20200515_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customorder',
            name='fig',
        ),
        migrations.RemoveField(
            model_name='customorder',
            name='usr',
        ),
        migrations.AddField(
            model_name='customorder',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='customorder',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
