from django.db import models

class Studnet(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    clas = models.IntegerField()