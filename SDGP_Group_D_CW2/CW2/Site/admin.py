from django.contrib import admin
from .models import Device, DeviceDetail, User, Booking

admin.site.register(Device)
admin.site.register(DeviceDetail)
admin.site.register(User)
admin.site.register(Booking)