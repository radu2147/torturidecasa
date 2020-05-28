# Generated by Django 3.0.4 on 2020-05-28 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_remove_address_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='addr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address_user', to='User.Address'),
        ),
    ]