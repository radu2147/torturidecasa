# Generated by Django 3.0.4 on 2020-07-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0008_wishlist_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date_of_order',
            field=models.DateField(default='2020-09-24'),
        ),
    ]
