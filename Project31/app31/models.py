from django.db import models


class Student(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    clas = models.IntegerField()
    total = models.IntegerField()
    average = models.DecimalField(max_digits=5,decimal_places=2)
    grade = models.CharField(max_length=2)
