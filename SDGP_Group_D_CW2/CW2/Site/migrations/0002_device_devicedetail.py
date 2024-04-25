#Generated by Django 4.2.3 on 2024-04-17 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceName', models.CharField(max_length=40)),
                ('deviceType', models.CharField(max_length=30)),
                ('deviceQuantity', models.IntegerField()),
                ('deviceAudit', models.DateField()),
                ('deviceLocation', models.CharField(max_length=20)),
                ('deviceStatus', models.CharField(blank=True, max_length=40)),
                ('deviceComments', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceSerial', models.CharField(blank=True, max_length=15)),
                ('deviceRAM', models.CharField(blank=True, max_length=40)),
                ('deviceCPU', models.CharField(blank=True, max_length=40)),
                ('deviceGPU', models.CharField(blank=True, max_length=40)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site.device')),
            ],
        ),
    ]