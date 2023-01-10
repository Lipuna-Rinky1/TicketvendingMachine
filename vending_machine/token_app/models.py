from django.db import models
from datetime import datetime


class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length= 50)
    designation = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length= 50, null=True)
    contact_no = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Token(models.Model):
    token = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True)
    patient_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.token

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.first_name

