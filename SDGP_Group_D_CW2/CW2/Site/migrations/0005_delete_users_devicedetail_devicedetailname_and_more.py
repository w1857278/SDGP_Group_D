# Generated by Django 4.2.3 on 2024-04-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0004_delete_users_alter_device_devicecomments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicedetail',
            name='deviceDetailName',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='device',
            name='deviceName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='devicedetail',
            name='deviceSerial',
            field=models.CharField(max_length=20),
        ),
    ]
