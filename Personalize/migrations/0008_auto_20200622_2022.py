# Generated by Django 3.0.4 on 2020-06-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personalize', '0007_customorder_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customorder',
            name='date',
            field=models.DateField(),
        ),
    ]