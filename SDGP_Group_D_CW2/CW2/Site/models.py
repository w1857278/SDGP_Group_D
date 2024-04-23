from django.db import models

class Users(models.Model):
    userDOB = models.DateField()
    userEmail = models.CharField(max_length = 200)
    userPassword = models.CharField(max_length = 200)
    userPermissions = models.CharField(max_length = 200, blank=True)
class Booking(models.Model):
    userID = models.ForeignKey('Users', on_delete=models.CASCADE)
    deviceID = models.ForeignKey('Device', on_delete=models.CASCADE)
    bookingType = models.CharField(max_length=50)
    dueDate = models.DateField()

class Device(models.Model):
    deviceName = models.CharField(max_length=40)
    deviceType = models.CharField(max_length = 30)
    deviceQuantity = models.IntegerField()
    deviceAudit = models.DateField()
    deviceLocation = models.CharField(max_length = 20)
    deviceStatus = models.CharField(max_length=40, blank=True)
    deviceComments = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.deviceName
        

class DeviceDetail(models.Model):
    device = models.ForeignKey('Device', on_delete=models.CASCADE)
    deviceSerial = models.CharField(max_length = 15, blank=True)
    deviceRAM = models.CharField(max_length=40, blank=True)
    deviceCPU = models.CharField(max_length=40, blank=True)
    deviceGPU = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return Device.deviceName + ' - Serial: ' + self.deviceSerial