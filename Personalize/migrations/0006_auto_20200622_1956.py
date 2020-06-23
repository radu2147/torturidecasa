# Generated by Django 3.0.4 on 2020-06-22 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personalize', '0005_auto_20200622_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customorder',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='customorder',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='customorder',
            name='tort',
            field=models.ImageField(upload_to='products/custom/'),
        ),
    ]
