# Generated by Django 4.2.3 on 2024-04-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0003_delete_users_devicedetail_devicedetailname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='deviceComments',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='device',
            name='deviceLocation',
            field=models.CharField(max_length=30),
        ),
    ]