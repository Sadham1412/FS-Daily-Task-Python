from django.db import models

# Create your models here.
class usersdetails(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

class AdminDeteils(models.Model):
    adminname=models.CharField(max_length=255)
    adminpass=models.CharField(max_length=100)
    