# Generated by Django 3.0.4 on 2020-08-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0016_auto_20200825_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produs',
            name='ident',
            field=models.IntegerField(unique=True),
        ),
    ]
