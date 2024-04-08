from django.db import models

class Users(models.Model):
    userDOB = models.DateField()
    userEmail = models.CharField(max_length = 200)
    userPassword = models.CharField(max_length = 200)
    userPermissions = models.CharField(max_length = 200)