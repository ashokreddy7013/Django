from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=50)
    contactno = models.IntegerField(primary_key=True)


