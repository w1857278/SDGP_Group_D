from django import forms
from .models import Device, DeviceDetail

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['deviceName', 'deviceType', 'deviceQuantity', 'deviceAudit', 'deviceLocation', 'deviceStatus', 'deviceComments']

class DeviceDetailsForm(forms.ModelForm):
    class Meta:
        model = DeviceDetail
        fields = ['deviceSerial', 'deviceRAM', 'deviceCPU','deviceGPU']
