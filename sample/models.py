from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    number = models.IntegerField()
