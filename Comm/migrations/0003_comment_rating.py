# Generated by Django 3.0.4 on 2020-05-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comm', '0002_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
