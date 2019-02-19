from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=50)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    public = models.ManyToManyField(Publication)
