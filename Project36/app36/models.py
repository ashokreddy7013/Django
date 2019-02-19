from django.db import models


class EmployeeReg(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
