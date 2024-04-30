from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    deviceID = models.ForeignKey('Device', on_delete=models.CASCADE)
    bookingType = models.CharField(max_length=50)
    dueDate = models.DateField()

    def __str__(self):
        return self.userID + ' ' + self.deviceID
    
class Device(models.Model):
    deviceName = models.CharField(max_length=50)
    deviceType = models.CharField(max_length = 30)
    deviceQuantity = models.IntegerField()
    deviceAudit = models.DateField()
    deviceLocation = models.CharField(max_length = 30)
    deviceStatus = models.CharField(max_length=40, blank=True)
    deviceComments = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.deviceName
        
class DeviceDetail(models.Model):
    device = models.ForeignKey('Device', on_delete=models.CASCADE)
    deviceDetailName = models.CharField(max_length=50, default=" ")
    deviceSerial = models.CharField(max_length = 20)
    deviceRAM = models.CharField(max_length=40, blank=True)
    deviceCPU = models.CharField(max_length=40, blank=True)
    deviceGPU = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return Device.deviceName + ' - Serial: ' + self.deviceSerial
    
class User(models.Model):
    email = models.EmailField(('email address'), blank=False)
    password = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.fname + 'Name: ' + self.lname
    