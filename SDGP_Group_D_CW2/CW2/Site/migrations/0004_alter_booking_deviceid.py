# Generated by Django 5.0.4 on 2024-04-27 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0003_booking_delete_bookings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='deviceID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Site.device'),
        ),
    ]
