from django.contrib import admin
from .models import Device, DeviceDetail, Booking

admin.site.register(Device)
admin.site.register(DeviceDetail)
admin.site.register(Booking)